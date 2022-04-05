
const N = 70;
const START_NODE = 0;
const RATE = 10;
const DISTANCE = 40;
const CIRCLE_SIZE = 8;
let runStepInterval = 50;

const nodes = [];
let running = false;
let nextStepTime = null;
let algo = null;

let simulation;

const runStopButton = document.querySelector('#toggle-run');
const stepButton = document.querySelector('#step');
const intervalInput = document.querySelector('#interval');
const bfsRadio = document.querySelector('#bfs');
const dijkstraRadio = document.querySelector('#dijkstra');

function BFS() {
  this.reset();
}

BFS.prototype.algorithm = function* () {
  let current = this.queue.shift();
  while (current !== undefined) {
    current.visited = true;
    current.isCurrent = true;
    yield;
    const tail = current.neighbors.filter(
      neighbor => !neighbor.visited && !this.queue.includes(neighbor));
    for (let n of tail) {
      this.queue.push(n);
      yield;
    }
    current.isCurrent = false;
    current = this.queue.shift();
  }
};

BFS.prototype.reset = function () {
  this._gen = this.algorithm();
  this.isDone = false;
  this.queue = [nodes[START_NODE]];
}

BFS.prototype.update = function () {
  const node = svg.select('#nodes')
    .selectAll('g')
    .data(nodes);
  node.select('circle')
      .classed('queued', d => this.queue.includes(d))
      .classed('visited', d => d.visited)
      .classed('current', d => d.isCurrent);
  node.select('text')
      .text('');
}

BFS.prototype.next = function () {
  const result = this._gen.next();
  if (result.done) {
    this.isDone = true;
  }
  return result;
}

function Dijkstra() {
  this.reset();
}

Dijkstra.prototype._lowestCost = function () {
  const eligible = Array.from(this.cost.entries())
    .filter(([n,]) => !n.visited);
  if (eligible.length === 0) {
    return undefined;
  }
  return eligible.sort(([, a], [, b]) => {
    return a - b;
  })[0][0];
}

Dijkstra.prototype.algorithm = function* () {
  let current = this._lowestCost();
  while (current !== undefined) {
    current.isCurrent = true;
    const cost = this.cost.get(current);
    yield;
    for (let i = 0; i < current.neighbors.length; i++) {
      const n = current.neighbors[i];
      const newCost = 1 + cost;
      if (this.cost.get(n) > newCost) {
        n.isCurrent = true;
        this.cost.set(n, newCost);
        yield;
        n.isCurrent = false;
      }
    }
    current.visited = true;
    current.isCurrent = false;
    current = this._lowestCost();
  }
};

Dijkstra.prototype.reset = function () {
  this._gen = this.algorithm();
  this.isDone = false;
  this.queue = [nodes[START_NODE]];
  this.cost = new Map(nodes.map(n => [n, n === nodes[START_NODE] ? 0 : Infinity]));
}

Dijkstra.prototype.update = function () {
  const node = svg.select('#nodes')
    .selectAll('g')
    .data(nodes);

  node.select('text')
      .text(d => {
    const cost = this.cost.get(d);
    return cost === Infinity ? '∞' : cost
  })
  .attr('font-size', 10)
      .attr('x', -4)
      .attr('y', '.3em');

  node.select('circle')
      .classed('queued', d => this.queue.includes(d))
      .classed('visited', d => d.visited && this.cost.get(d) < Infinity)
      .classed('current', d => d.isCurrent);
}

Dijkstra.prototype.next = function () {
  const result = this._gen.next();
  if (result.done) {
    this.isDone = true;
  }
  return result;
}

function reset() {
  nodes.forEach(n => {
    n.visited = false;
    n.isCurrent = false;
  });
}

function stop() {
  nextStepTime = null;
  running = false;
}

function run() {
  nextStepTime = null;
  running = true;
  requestAnimationFrame(step);
}

function toggleRun() {
  if (running) {
    stop();
  } else {
    run();
  }
}

function step(timestamp) {
  if (!running) {
    return;
  }

  if (algo.isDone) {
    reset();
    algo.reset();
  }

  if (nextStepTime === null) {
    nextStepTime = timestamp;
  }
  
  while (nextStepTime <= timestamp) {
    const { done } = algo.next();
    if (done) {
      stop();
      update();
      return;
    }
    nextStepTime += runStepInterval;
  }
  update();
  requestAnimationFrame(step);
}

/**
 * Event listeners
 */
document.querySelector('#reset').addEventListener('click', () => {
  stop();
  algo.reset();
  reset(); 
  update();
});

document.querySelector('#graph-1').addEventListener(
  'click', () => newGraph(createGraph1)
);

document.querySelector('#graph-2').addEventListener(
  'click', () => newGraph(createGraph2)
);

document.querySelector('#graph-3').addEventListener(
  'click', () => newGraph(createGraph3)
);

runStopButton.addEventListener('click', () => {
  toggleRun();
  update();
});

stepButton.addEventListener(
  'click', () => {
    if (algo.isDone) {
      reset();
      algo.reset();
    }
    algo.next();
    update();
  }
);

intervalInput.addEventListener(
  'input', (e) => {
    runStepInterval = parseInt(e.target.value);
  }
)

bfsRadio.addEventListener(
  'change', () => {
    algo = new BFS();
    stop();
    reset();
    update();
  }
)

dijkstraRadio.addEventListener(
  'change', () => {
    algo = new Dijkstra();
    stop();
    reset();
    update();
  }
)

/**
 * Graph creation functions
 */
function createGraph1() {
  // Horrible horrible code
  const to = new Set();
  const from = new Set(Array.from({length: N}, (_, i) => i));
  const nodes = Array.from({length: N}, (_, i) => {return {id: i, neighbors: []}});
  to.add(nodes[0]);
  for (let u = 0; u < N; u++) {
    const y = parseInt(Math.random() * to.size);
    const o = parseInt(Math.random() * from.size);
    const r = Array.from(from)[o];
    Array.from(to)[y].neighbors.push(nodes[r]);
    to.add(nodes[r]);
    from.delete(r);
  }
  for (let u = 0; u < N / 10; u++) {
    const a = parseInt(Math.random() * N);
    const b = parseInt(Math.random() * N);
    nodes[a].neighbors.push(nodes[b]);
  }
  return nodes;
}

function createGraph2() {
  const M = 8;
  const nodes = Array.from({length: N}, (_, i) => {return {id: i, neighbors: []}});
  for (let x = 0; (x + 1) * M < N; x++) {
    nodes[parseInt(x * M / 2)].neighbors = Array.from({length: M}, (_, i) => nodes[i + M * x + 1]);
  }
  return nodes;
}

function createGraph3() {
  const nodes = Array.from({length: N}, (_, i) => {return {id: i}});
  nodes.forEach((node, i) => {
    node.neighbors = [];
    const d = parseInt(Math.random() * N);
    const e = Math.min(Math.max(i + d, 0), N - 1);
    node.neighbors.push(nodes[d]);
    if (Math.random() < .3) { node.neighbors.push(nodes[parseInt(Math.random() * N)]) }
  });
  return nodes;
}

function newGraph(createGraphFn) {
  stop();
  if (simulation !== undefined) {
    simulation.stop();
  }
  nodes.length = 0;
  nodes.push(...createGraphFn());
  simulation = createSimulation();
  algo.reset();
}

function update() {
  stepButton.disabled = running;
  runStopButton.innerHTML = running ? "Stop" : "Run";
  intervalInput.value = runStepInterval;

  const link = svg.select('#links')
  .selectAll('line')
  .data(simulation.force('links').links());

  link.exit().remove();
  link.enter().append('line')
      .attr('marker-end', 'url(#arrow)')
    .merge(link)
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
  
  const node = svg.select('#nodes')
    .selectAll('g')
    .data(nodes);

  node.exit().remove();
  const gEnter = node.enter().append('g');
  gEnter.append('circle')
      .attr('r', CIRCLE_SIZE)
  gEnter.append('text');

  node.attr('transform', d => 'translate(' + d.x + ',' + d.y + ')');
  algo.update();
}

const svg = d3.select('svg');
svg.append("g").attr("id", "links");
svg.append("g").attr("id", "nodes");

function resize() {
  const width = window.innerWidth;
  const height = window.innerHeight;
  svg.attr('width', width).attr('height', height);
  simulation.force('center').x(width / 2).y(height / 2);
}

d3.select(window).on('resize', resize);

const defs = svg.append('defs');
const marker = defs.append('marker')
  .attr('id', 'arrow')
  .attr('markerHeight', 5)
  .attr('markerWidth', 5)
  .attr('markerUnits', 'strokeWidth')
  .attr('orient', 'auto')
  .attr('refX', 20)
  .attr('refY', 0)
  .attr('viewBox', '-5 -5 10 10')
  .append('path')
  .attr('d', 'M 0,0 m -5,-5 L 5,0 L -5,5 Z')
  .attr('fill', 'black');

function createSimulation() { 
  function f(node) {
    return node.neighbors.map(neighbor => ({source: node.id, target: neighbor.id}));
  }
  const links = [].concat(...nodes.map(f));
  return d3.forceSimulation(nodes)
    .force('center', d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2))
    .force('links', d3.forceLink(links).distance(DISTANCE))
    .force('charge', d3.forceManyBody())
    .on('tick', update);
}

algo = new BFS();
newGraph(createGraph1);
resize();
