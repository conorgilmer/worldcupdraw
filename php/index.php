<!-- header -->
<?php include('header.php'); ?>  

<!-- additional header stuff -->

  <script type="text/javascript">

  // Load the Visualization API and the chart package.
  google.load('visualization', '1', {'packages':['corechart']});
  function drawChart(num) {
   
    var jsonBounceData = $.ajax({
      url: "getbounces.php",
      data: "q="+num,
      dataType:"json",
      async: false
    }).responseText;


      // Bounce
      var bounce_data = new google.visualization.DataTable(jsonBounceData);
      // Instantiate and draw our chart, passing in some options.
      var bounce_bar_chart = new google.visualization.BarChart(document.getElementById('bounce_bar_div'));
      bounce_bar_chart.draw(bounce_data, {title: 'Draw Pot Position', bars: 'horizontal',  width: 500, height: 340, legend: { position: 'none' },});


    }

    </script>



<!-- menu -->
<?php include('menu.php'); ?>  

<!-- Content Start -->

      <!-- Example row of columns -->
      <div class="row">
        <div class="col-lg-9">
 <h2>European Groups - World Cup Qualifying</h2>

  <form>
  <select name="users" onchange="drawChart(this.value)">
  <option value="">Select a Group :</option>
    <option value="A">Group A</option>
    <option value="B">Group B</option>
    <option value="C">Group C</option>
    <option value="D">Group D</option>
    <option value="E">Group E</option>
    <option value="F">Group F</option>
    <option value="G">Group G</option>
    <option value="H">Group H</option>
    <option value="I">Group I</option>
  </select>
  </form>
</div>
</div>
      <div class="row">
        <div class="col-lg-4">
        </div>
        <div class="col-lg-4">
  <div id="bounce_bar_div"></div>
        </div>
        <div class="col-lg-4">
        </div>
      </div>

<!-- Content End -->

<!-- footer -->
<?php include('footer.php'); ?>  
