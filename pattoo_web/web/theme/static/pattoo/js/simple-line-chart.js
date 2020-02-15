
function SimpleLineChart( url, heading, y_label, div_id ) {
    //  url: URL from which to retrieve data.tsv file
    //  heading: Heading for chart
    //  y_label: Label to use for y axis
    //  div_id: DIV ID for chart

    // set the dimensions and margins of the graph
    var margin = {top: 20, right: 50, bottom: 50, left: 75};
    var headingVOffset = 0;
    var outerWidth = 950;
    var outerHeight = 400;
    var innerWidth = outerWidth - margin.left - margin.right;
    var innerHeight = outerHeight - margin.top - margin.bottom;

    // Define where we are placing the chart
    //var div_id = '#pattoo_simple_line_chart'

    // Setup standard colors
    var standard_colors = d3.scaleOrdinal(d3.schemeCategory10);

    // Append the svg obgect to the body of the page
    // Define the limits of the SVG canvas
    var svg = d3.select(div_id).append('svg')
      .attr('width', outerWidth)
      .attr('height', outerHeight);

    // Define the graph area on the canvas
    // Appends a 'group' element to 'svg'
    // Moves the 'group' element to the top left margin
    var g = svg.append('g')
      .attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')');

    // Set scales and colors for chart area
    var x = d3.scaleTime().range([0, innerWidth]),
        y = d3.scaleLinear().range([innerHeight, 0]);

    // .defined(d => !isNaN(d.value))
    // .defined(function(d) { return !isNaN(d.value); })
    // .defined(function(d){return d.value !== null && d.value !== undefined})
    // .defined(function(d) { return d.value; })
    // .data(data.filter(function(d) { return d; }))
    // .defined(function(d) { return d.value != null; })

    // Define the line
    var line = d3.line()
        .defined(function(d) { return d; })
        .curve(d3.curveBasis)
        .x(function(d) {return x(d.timestamp);})
        .y(function(d) {return y(d.value);});

    // Get the data
    d3.json(url, (error, data) => {
      if (error) throw error;

      // Format the data
      data.forEach(function(d) {
           d.timestamp = new Date(d.timestamp);
           d.value = +d.value;
       });

      // Scale the range of the data
      x.domain(d3.extent(data, d => d.timestamp));
      y.domain([0, d3.max(data, d => Math.max(d.value))]);

      // Add the line path.
      g.append('path')
          .datum(data)
          .attr('class', 'line')
          .attr('d', line)
          .attr('fill', 'none')
          .style('stroke-width', 2)
          .style('stroke', function(d) { return standard_colors(); });

      // Define formatting for X axis lines and labels
      g.append('g')
          .attr('class', 'axisChart')
          .attr('transform', 'translate(0,' + innerHeight + ')')
          .call(d3.axisBottom(x)
          .tickFormat(d3.timeFormat('%Y-%m-%d %H:%M')))
          .selectAll('text')
          .style('font', '10px Nunito')
          .style('text-anchor', 'end')
          .attr('dx', '-.8em')
          .attr('dy', '.15em')
          .attr('transform', "rotate(-20)");

      // Define formatting for Y axis lines and labels (Rotation)
      g.append('g')
          .attr('class', 'axisChart')
          .call(d3.axisLeft(y))
          .append('text')
          .attr('transform', 'rotate(-90)')
          .attr('y', 6)
          .attr('dy', '0.71em')
          .attr('fill', '#000000')
          .text(y_label);

    });

}
