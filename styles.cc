body {
  margin: 0 0;
  padding: 0 0;
  background: #d7d7db;
}

form {
  float: right;
  position: absolute;
  top: 0;
  right: 0;
  display: inline-block;
  vertical-align: top;
  border: 1px solid #b1b1b3;
  border-radius: 1em;
  padding: 1em;
}

form fieldset {
  margin-top: .5em;
}

#interval {
  direction: rtl;
}

svg {
  background: #d7d7db;
  display: inline-block;
}

circle {
  fill: #bbb;
  stroke-width: 2;
  stroke: black;
}

circle.queued {
  fill: #ff9400;
}

circle.visited {
  fill: #55c1ff;
}

circle.current {
  fill: yellow;
  stroke: red;
  stroke-width: 2;
}

line {
  stroke-width: 1.5;
  stroke: #444;
}

text {
  fill: black;
}
