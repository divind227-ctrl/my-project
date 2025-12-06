
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Design Mech and Purchase Box</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      display: flex;
      flex-direction: column; /* Stack the rows vertically */
      align-items: center;
      height: 100vh;
      padding: 20px;
      gap: 20px;
    }

    .row {
      display: flex;
      justify-content: space-evenly;
      gap: 20px;
      width: 100%;
      max-width: 900px; /* Limit the maximum width */
    }

    .box {
      width: 100%;
      max-width: 220px;
      min-height: 300px;
      padding: 20px;
      background-color: #fff;
      border: 1px solid #ccc;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      display: flex;
      flex-direction: column;
      height: 300px;
      overflow-y: auto;
      margin: 10px;
    }

    .heading {
      font-size: 16px; 
      font-weight: bold;
      color: #333;
      margin-bottom: 15px;
    }

    .Design_Mech, .purchase, .Design_elec, .store, .process, .Marketing, .Proposal, .HR {
      font-size: 12px; 
      color: #333;
      margin-bottom: 10px;
    }

    .label {
      font-weight: bold;
      display: inline-block;
      margin-right: 5px;
    }

    .value {
      color: #007BFF;
    }

    .details-button {
      position: absolute;
      top: 10px;
      right: 10px;
      padding: 6px 12px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 10px; 
    }

    .details-button:hover {
      background-color: #0056b3;
    }

    .date-container {
      display: flex;
      justify-content: flex-start;
      margin-bottom: 10px;
      gap: 10px;
      width: 100%;
    }

    .date-input {
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 12px; 
      width: 100px;
    }

    /* Form Styling */
    form {
      width: 70%;
      max-width: 250px;
      margin-bottom: 20px;
    }

    button[type="submit"] {
      background-color: #007BFF;
      color: white;
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px; 
      margin-top: 10px;
    }

    button[type="submit"]:hover {
      background-color: #0056b3;
    }

    .box {
      padding: 20px;
      border: 2px solid #ccc;
      background-color: #f9f9f9;
      width: 100%;
      margin: 0 auto;
    }

    .box .heading {
      margin-bottom: 20px;
      color: #333;
      font-size: 24px;
    }

    /* Adjust the HR box styling */
    .HR {
        display: block; /* Default block layout */
        align-items: flex-start; /* Align items to the left */
        justify-content: flex-start; /* Keep content aligned to top-left */
    }

    .flowchart {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        width: 100%;
    }

    .flow-step {
        background-color: #fff;
        border-radius: 10px;
        border: 2px solid #ccc;
        padding: 15px;
        width: 250px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        position: relative;
    }

    .flow-step .label {
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
    }

    .flow-step .value {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }

    .arrow-down {
        width: 0;
        height: 0;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-top: 10px solid #ccc;
        margin: 10px auto;
    }

    .sub-info {
        display: flex;
        flex-direction: column;
        margin-top: 10px;
        gap: 5px;
    }

    .sub-info-part {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: #555;
    }

    .sub-info-part .label {
        color: #888;
    }

    .sub-info-part .value {
        font-weight: bold;
    }

    .footer {
        margin-top: 40px;
        font-size: 14px;
        color: #777;
    }

  </style>
</head>
<body>
  <!-- Top Row -->
  <div class="row">
    <div class="box Design_Mech">
      <div class="heading">Design Mech</div>
      <div class="Design_Mech">Details about Design Mech</div>
    </div>
    <div class="box purchase">
      <div class="heading">Purchase</div>
      <div class="purchase">Details about Purchase</div>
    </div>
    <div class="box Design_elec">
      <div class="heading">Design Elec</div>
      <div class="Design_elec">Details about Design Elec</div>
    </div>
    <div class="box store">
      <div class="heading">Store</div>
      <div class="store">Details about Store</div>
    </div>
  </div>

  <!-- Bottom Row -->
  <div class="row">
    <div class="box process">
      <div class="heading">Process</div>
      <div class="process">Details about Process</div>
    </div>
    <div class="box Marketing">
      <div class="heading">Marketing</div>
      <div class="Marketing">Details about Marketing</div>
    </div>
    <div class="box Proposal">
      <div class="heading">Proposal</div>
      <div class="Proposal">Details about Proposal</div>
    </div>
    <div class="box HR">
      <div class="heading">HR</div>
      <div class="HR">Details about HR</div>
    </div>
  </div>
</body>
</html>








