// Wait for DOM and Konva to load
window.addEventListener('load', function() {
    // Check if Konva loaded properly
    if (typeof Konva === 'undefined') {
        document.getElementById('loading').innerHTML = 
            'Error: Could not load Konva library. Please check your internet connection.';
        return;
    }

    // Hide loading message
    document.getElementById('loading').style.display = 'none';

    // Parsing JSON containing table data from database
    var tables_json = JSON.parse(document.getElementById('tables_json').textContent);
    var users_json = JSON.parse(this.document.getElementById('users_json').textContent);

    // Initializing empty arrays to hold table data
    var tables = []
    var names = []
    var name_id = {}

    console.log('Tables');
    console.log(tables);
    console.log('Tables JSON');
    console.log(tables_json);
    
    users_json.forEach((user) => {
        names.push(user.first_name + ' ' + user.last_name)

        names.forEach((name) => {
            name_id[name] = user.id;
        })
    })

    var iterateX = 0

    var x = [100, 550]
    var circle_y = 120
    var rect_y = 80

    var json_index = 0;

    tables_json.forEach((element) => {
        if (element.shape =='circle'){
        tables.push({
            id: element.tableID, type: element.shape, x:x[iterateX], y:circle_y, radius: 40, status: element.table_status, seats: element.seats, guests: element.guests, waiter: choices = names, elapsedTime: 0, startTime: 0, isRunning: false, index: json_index})

            if (x[iterateX] == 100){
                iterateX += 1;
            }
            else if(x[iterateX] == 550){
                iterateX = 0;
                circle_y += 100;
            }

        }else if (element.shape == 'rect'){
            tables.push({
                id: element.tableID, type: element.shape, x:300, y:rect_y, width: 120, height: 60, status: element.table_status, seats: element.seats, guests: element.guests, waiter: choices = names, elapsedTime: 0, startTime: 0, isRunning: false, index: json_index})
            
            rect_y += 100;
        }
        json_index++;
    });

    
    // Added timer-related variables
    /*const tables = [
        // Circular tables arranged in left column (increased radius to 40)
        { id: 1, type: 'circle', x: 100, y: 100, radius: 40, status: 'Occupied', seats: 10, guests: 8, waiter: 'John T.', elapsedTime: 0, startTime: 0, isRunning: false },
        { id: 2, type: 'circle', x: 100, y: 300, radius: 40, status: 'Available', seats: 6, guests: 0, waiter: 'N/A', elapsedTime: 0, startTime: 0, isRunning: false },
        { id: 3, type: 'circle', x: 100, y: 500, radius: 40, status: 'Available', seats: 6, guests: 0, waiter: 'N/A', elapsedTime: 0, startTime: 0, isRunning: false },
        
        // Rectangular tables for 4 people in middle column (increased size and added more tables)
        { id: 4, type: 'rect', x: 300, y: 80, width: 120, height: 60, status: 'Occupied', seats: 4, guests: 4, waiter: 'Sarah M.',  elapsedTime: 0, startTime: 0, isRunning: false  },
        { id: 5, type: 'rect', x: 300, y: 200, width: 120, height: 60, status: 'Available', seats: 4, guests: 0, waiter: 'N/A',  elapsedTime: 0, startTime: 0, isRunning: false  },
        { id: 9, type: 'rect', x: 300, y: 320, width: 120, height: 60, status: 'Available', seats: 4, guests: 0, waiter: 'N/A',  elapsedTime: 0, startTime: 0, isRunning: false  },
        { id: 10, type: 'rect', x: 300, y: 440, width: 120, height: 60, status: 'Reserved', seats: 4, guests: 0, waiter: 'Lisa R.',  elapsedTime: 0, startTime: 0, isRunning: false  },
        { id: 11, type: 'rect', x: 300, y: 560, width: 120, height: 60, status: 'Available', seats: 4, guests: 0, waiter: 'N/A',  elapsedTime: 0, startTime: 0, isRunning: false  },
        
        // Small rectangular tables for 2 people in right column (slightly increased size)
        { id: 6, type: 'rect', x: 550, y: 100, width: 50, height: 70, status: 'Available', seats: 2, guests: 0, waiter: 'N/A',  elapsedTime: 0, startTime: 0, isRunning: false  },
        { id: 7, type: 'rect', x: 550, y: 300, width: 50, height: 70, status: 'Occupied', seats: 2, guests: 2, waiter: 'Mike P.',  elapsedTime: 0, startTime: 0, isRunning: false  },
        { id: 8, type: 'rect', x: 550, y: 500, width: 50, height: 70, status: 'Available', seats: 2, guests: 0, waiter: 'N/A',  elapsedTime: 0, startTime: 0, isRunning: false }
    ];*/


    // Initialize Konva Stage with larger dimensions
    const stage = new Konva.Stage({
        container: 'stage-container',
        width: 800,
        height: 700  // Increased height to accommodate larger tables
    });

    const layer = new Konva.Layer();
    stage.add(layer);

    // Get tooltip and editor elements
    const tooltip = document.getElementById('tooltip');
    const editorContent = document.getElementById('editor-content');
    let selectedShape = null;

    function showTooltip(table) {
        const mousePos = stage.getPointerPosition();
        const containerRect = stage.container().getBoundingClientRect();
    
        // Only display the timer for the hovered table
        const hrs = Math.floor(table.elapsedTime / (1000 * 60 * 60));
        const mins = Math.floor(table.elapsedTime / (1000 * 60) % 60);
        const secs = Math.floor(table.elapsedTime / 1000 % 60);
    
        const formattedTime = `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    
        tooltip.dataset.tableId = table.id; // Store table ID for comparison in updateTimer
    
        tooltip.innerHTML = `
            Table ID: ${table.id}<br>
            Seats: ${table.seats}<br>
            Guests: ${table.guests}<br>
            Assigned waiter: ${table.waiter}<br>
            Status: ${table.status}<br>
            Timer: ${formattedTime}<br>
        `;
        
        tooltip.style.display = 'block';
        tooltip.style.left = (mousePos.x + containerRect.left + 20) + 'px';
        tooltip.style.top = (mousePos.y + containerRect.top + 20) + 'px';
    }
    
    function hideTooltip() {
        tooltip.style.display = 'none';
    }

    function showEditor(table, shape) {
        // Deselect previously selected shape
        if (selectedShape) {
            selectedShape.strokeWidth(0);
            layer.draw();
        }

        // Highlight selected shape
        shape.strokeWidth(2);
        shape.stroke('#000');
        selectedShape = shape;
        layer.draw();
        
        // Create editor form
        editorContent.innerHTML = `
            <div class="form-group">
                <label>Status:</label>
                <select id="table-status">
                    <option value="Available" ${table.status === 'Available' ? 'selected' : ''}>Available</option>
                    <option value="Occupied" ${table.status === 'Occupied' ? 'selected' : ''}>Occupied</option>
                    <option value="Reserved" ${table.status === 'Reserved' ? 'selected' : ''}>Reserved</option>
                </select>
            </div>
            <div class="form-group">
                <label>Number of Guests:</label>
                <select id="table-guests">
                </select>
            </div>
            <div class="form-group">
                <label>Assigned Waiter:</label>
                <select id="table-waiter">
                </select>
            </div>
            <div class="form-group">
                <button onclick="updateTable(${table.id})">Update Table</button>
                <button class="cancel" onclick="cancelEdit()">Cancel</button>
            </div>
            <div class="form-group">
                <button onclick="startTimer(${table.id})">Start Timer</button> 
                <button class="cancel" onclick="resetTimer(${table.id})">Reset Timer</button>            
            </div>
        `;
        var table_waiter = document.getElementById('table-waiter');

        names.forEach((name) => {
            let option = document.createElement("option");
            option.textContent = name;
            option.value = name;
            table_waiter.appendChild(option);
        })

        var table_guests = document.getElementById('table-guests');

        for (let i = 0; i <= table.seats; i++){
            let option = document.createElement("option");
            option.textContent = i;
            table_guests.appendChild(option);
        } 
    }

    // Global functions for the editor

    window.startTimer = function(tableId) {
        const table = tables.find(t => t.id === tableId);
        if (!table || table.isRunning) return;  // If the table is not found or timer is already running
    
        table.startTime = Date.now() - table.elapsedTime;
        table.isRunning = true;
        table.timer = setInterval(() => updateTimer(tableId), 10);
    }
    

    window.updateTimer = function(tableId) {
        const table = tables.find(t => t.id === tableId);
        if (!table) return;
    
        const currentTime = Date.now();
        table.elapsedTime = currentTime - table.startTime;
    
        const hrs = Math.floor(table.elapsedTime / (1000 * 60 * 60));
        const mins = Math.floor(table.elapsedTime / (1000 * 60) % 60);
        const secs = Math.floor(table.elapsedTime / 1000 % 60);
    
        const formattedTime = `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    
        // Only update the tooltip if it's currently displayed and for the correct table
        if (tooltip.style.display === 'block' && tooltip.dataset.tableId == tableId) {
            tooltip.innerHTML = `
                Table ID: ${table.id}<br>
                Seats: ${table.seats}<br>
                Guests: ${table.guests}<br>
                Assigned waiter: ${table.waiter}<br>
                Status: ${table.status}<br>
                Timer: ${formattedTime}<br>
            `;
        }
    }
    

    window.resetTimer = function(tableId) {
        const table = tables.find(t => t.id === tableId);
        if (!table) return;
    
        clearInterval(table.timer);
        table.elapsedTime = 0;
        table.startTime = 0;
        table.isRunning = false;
    
        // Reset tooltip timer
        if (tooltip.style.display === 'block') {
            tooltip.innerHTML = '00:00:00';
        }
    }
    


    window.updateTable = function(tableId) {
        const table = tables.find(t => t.id === tableId);
        if (!table) return;

        // Update table data
        table.status = document.getElementById('table-status').value;
        table.guests = parseInt(document.getElementById('table-guests').value);
        table.waiter = document.getElementById('table-waiter').value;

        /*updated_table = tables.find(t => t.id === tableId);

        console.log('Updated Table');
        console.log(updated_table);

        updated_table['table_status'] = table.status
        updated_table['guests'] = table.guests
        updated_table['employee_id'] = name_id[document.getElementById('table-waiter').value];*/

        target_table = tables_json[table.index];

        target_table['table_status'] = table.status;
        target_table['guests'] = table.guests;
        target_table['employee_id'] = name_id[document.getElementById('table-waiter').value];

        tables_json[table.index]['']

        console.log('Updated Table JSON')
        console.log(tables_json)




        // Update shape color
        const shape = selectedShape;
        if (shape) {
            shape.fill(table.status === 'Occupied' ? '#dc2626' : 
                      table.status === 'Reserved' ? '#f59e0b' : '#22c55e');
            shape.strokeWidth(0);
            layer.draw();
        }

        // Reset selection
        selectedShape = null;
        editorContent.innerHTML = '<p class="no-selection">Click a table to edit its details</p>';
    };

    window.cancelEdit = function() {
        if (selectedShape) {
            selectedShape.strokeWidth(0);
            layer.draw();
            selectedShape = null;
        }
        editorContent.innerHTML = '<p class="no-selection">Click a table to edit its details</p>';
    };

    // Create tables
    tables.forEach(table => {
        let shape;
        const isOccupied = table.status === 'Occupied';
        const isReserved = table.status === 'Reserved';
        const fill = isOccupied ? '#dc2626' : 
                    isReserved ? '#f59e0b' : '#22c55e';

        if (table.type === 'circle') {
            shape = new Konva.Circle({
                x: table.x + table.radius,
                y: table.y + table.radius,
                radius: table.radius,
                fill: fill,
                shadowColor: 'black',
                shadowBlur: 5,
                shadowOpacity: 0.2,
            });
        } else {
            shape = new Konva.Rect({
                x: table.x,
                y: table.y,
                width: table.width,
                height: table.height,
                fill: fill,
                shadowColor: 'black',
                shadowBlur: 5,
                shadowOpacity: 0.2,
            });
        }

        // Add hover effects
        shape.on('mouseenter', function() {
            document.body.style.cursor = 'pointer';
            if (this !== selectedShape) {
                this.opacity(0.8);
                layer.draw();
            }
            showTooltip(table, event);
        });

        shape.on('mouseleave', function() {
            document.body.style.cursor = 'default';
            if (this !== selectedShape) {
                this.opacity(1);
                layer.draw();
            }
            hideTooltip();
        });

        shape.on('mousemove', function() {
            showTooltip(table, event);
        });

        // Add click handler for editing
        shape.on('click', function() {
            showEditor(table, this);
        });

        layer.add(shape);
    });

    // Initial draw
    layer.draw();
});