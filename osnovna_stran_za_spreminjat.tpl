
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>SUDOKU</title>
    
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    
    <style type="text/css">
    
      body, html {
        background-image: url(https://cdn.pixabay.com/photo/2020/09/15/15/52/background-5574014_1280.png);
      }

      table {
        border: 2px solid #000000;
        width: 500px;
        height: 500px;
        position: absolute;
        left: 30%;
        top: 20%;        
      }



      td {
        border: 1px solid #000000;
        text-align: center;
        vertical-align: middle; 
        background-color: white; 
      }

      input {
        color: #000000;
        padding: 0;
        border: 0;
        text-align: center;
        width: 100%;
        height: 100%;
        font-size: 24px;
        background-color: #FFFFFF;
        outline: none;
        box-sizing: border-box;
        margin: 0px;
        padding: 0px;
      }

      .naslov {
        position: absolute;
        left: 29.5%;
        top: 3%;
        
      }

      .napake {
        position: absolute;
        top: 620px;

      }

      /* Dropdown Button */
      .dropbtn {
        background-color: #04AA6D;
        color: white;
        padding: 16px;
        font-size: 16px;
        border: none;
      }
      
      /* The container <div> - needed to position the dropdown content */
      .dropdown {
        position: relative;
        display: inline-block;
      }
      
      /* Dropdown Content (Hidden by Default) */
      .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
      }
      
      /* Links inside the dropdown */
      .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
      }
      
      /* Change color of dropdown links on hover */
      .dropdown-content a:hover {background-color: #ddd;}
      
      /* Show the dropdown menu on hover */
      .dropdown:hover .dropdown-content {display: block;}
      
      /* Change the background color of the dropdown button when the dropdown content is shown */
      .dropdown:hover .dropbtn {background-color: #3e8e41;}

      input:disabled {
        background-color: #EEEEEE;
      }

      td:nth-child(3n) {
          border-right:4px solid ;

      }
      tr td:nth-child(1){
          border-left: 4px solid;
      }

      tr:nth-child(3n){
          border-bottom: 4px solid;
      }

      tr:nth-child(1){
          border-top: 4px solid;
      }
      


    </style>
  </head>
  <body>

        <div class="dropdown">
          <button class="dropbtn">NOVA IGRA</button>
          <div class="dropdown-content">
            <a href="/nova-igra-1">Lahka</a>
            <a href="/nova-igra-2">Srednja</a>
            <a href="/nova-igra-3">Težka</a>
          </div>
        </div>

        <h1 class="naslov">NEDELJSKI SUDOKU S TIMOM</h1>

          <table id="grid" class="center">


        % for i, vrstica in enumerate(sudokuseznam):

            <tr>
              % if sudokuseznam[i][0] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 0}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 0}"}} type="text">
                </form>
              </td>
              % else:
              <td><input id={{f"cell-{9 * i + 0}"}} name={{f"cell-{9 * i + 0}"}}  type="text" value={{sudokuseznam[i][0]}} disabled></td>
              % end

              % if sudokuseznam[i][1] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 1}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 1}"}} type="text" id={{f"cell-{9 * i + 1}"}}></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 1}"}} name={{f"cell-{9 * i + 1}"}} type="text" value={{sudokuseznam[i][1]}} disabled></td>
              % end

              % if sudokuseznam[i][2] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 2}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 2}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 2}"}} name={{f"cell-{9 * i + 2}"}} type="text" value={{sudokuseznam[i][2]}} disabled></td>
              % end

              % if sudokuseznam[i][3] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 3}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 3}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 3}"}} name={{f"cell-{9 * i + 3}"}} type="text" value={{sudokuseznam[i][3]}} disabled></td>
              % end

              % if sudokuseznam[i][4] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 4}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 4}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 4}"}} name={{f"cell-{9 * i + 4}"}} type="text" value={{sudokuseznam[i][4]}} disabled></td>
              % end

              % if sudokuseznam[i][5] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 5}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 5}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 5}"}} name={{f"cell-{9 * i + 5}"}} type="text" value={{sudokuseznam[i][5]}} disabled></td>
              % end

              % if sudokuseznam[i][6] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 6}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 6}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 6}"}} name={{f"cell-{9 * i + 6}"}} type="text" value={{sudokuseznam[i][6]}} disabled></td>
              % end

              % if sudokuseznam[i][7] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 7}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 7}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 7}"}} name={{f"cell-{9 * i + 7}"}}type="text" value={{sudokuseznam[i][7]}} disabled></td>
              % end

              % if sudokuseznam[i][8] == 0:
              <td>
                <form action="/dodaj/" id={{f"cell-{9 * i + 8}"}} autocomplete="off">
                  <input name={{f"cell-{9 * i + 8}"}} type="text"></td>
                </form>
              % else:
              <td><input id={{f"cell-{9 * i + 8}"}} name={{f"cell-{9 * i + 8}"}} type="text" value={{sudokuseznam[i][8]}} disabled></td>
              % end

            </tr>

        % end


          </table>
          <div class="napake">
            <h3>NEPRAVILNI POSKUSI: {{napake}}</h3>
          </div>
          <div class="score">
            <h3>TOČKE: {{score}}</h3>
          </div>
  </body>
</html>