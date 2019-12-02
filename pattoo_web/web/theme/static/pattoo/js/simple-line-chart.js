
function SimpleLineChart( url, heading ) {
    // set the dimensions and margins of the graph
    var margin = {top: 20, right: 40, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // Define where we are placing the chart
    var div_id = 'pattoo-simple-line-chart'

    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);

    // define the line
    var valueline = d3.line()
        .x((d) => x(d.date))
        .y((d) => y(d.value));

    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    var svg = d3.select(div_id).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

    // Get the data
    d3.json(url, (error, data) => {
      if (error) throw error;

      // format the data
      data.forEach(function(d) {
           d.timestamp = new Date(d.timestamp * 1000);
           d.value = +d.value;
       });

      // Scale the range of the data
      x.domain(d3.extent(data, d => d.date));
      y.domain([0, d3.max(data, d => Math.max(d.value))]);

      // Add the valueline path.
      svg.append("path")
          .data([data])
          .attr("class", "line")
          .attr("d", valueline);

      // Add the X Axis
      svg.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x));

      // Add the Y0 Axis
      svg.append("g")
          .attr("class", "axisSteelBlue")
          .call(d3.axisLeft(y));

    }).header("Content-Type", "application/json");
}
