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

    const tables = [
        // Circular tables arranged in left column (increased radius to 40)
        { id: 1, type: 'circle', x: 100, y: 100, radius: 40, status: 'occupied', seats: 10, guests: 8, waiter: 'John T.' },
        { id: 2, type: 'circle', x: 100, y: 300, radius: 40, status: 'available', seats: 6, guests: 0, waiter: 'N/A' },
        { id: 3, type: 'circle', x: 100, y: 500, radius: 40, status: 'available', seats: 6, guests: 0, waiter: 'N/A' },
        
        // Rectangular tables for 4 people in middle column (increased size and added more tables)
        { id: 4, type: 'rect', x: 300, y: 80, width: 120, height: 60, status: 'occupied', seats: 4, guests: 4, waiter: 'Sarah M.' },
        { id: 5, type: 'rect', x: 300, y: 200, width: 120, height: 60, status: 'available', seats: 4, guests: 0, waiter: 'N/A' },
        { id: 9, type: 'rect', x: 300, y: 320, width: 120, height: 60, status: 'available', seats: 4, guests: 0, waiter: 'N/A' },
        { id: 10, type: 'rect', x: 300, y: 440, width: 120, height: 60, status: 'reserved', seats: 4, guests: 0, waiter: 'Lisa R.' },
        { id: 11, type: 'rect', x: 300, y: 560, width: 120, height: 60, status: 'available', seats: 4, guests: 0, waiter: 'N/A' },
        
        // Small rectangular tables for 2 people in right column (slightly increased size)
        { id: 6, type: 'rect', x: 550, y: 100, width: 50, height: 70, status: 'available', seats: 2, guests: 0, waiter: 'N/A' },
        { id: 7, type: 'rect', x: 550, y: 300, width: 50, height: 70, status: 'occupied', seats: 2, guests: 2, waiter: 'Mike P.' },
        { id: 8, type: 'rect', x: 550, y: 500, width: 50, height: 70, status: 'available', seats: 2, guests: 0, waiter: 'N/A' }
    ];

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

    function showTooltip(table, evt) {
        const mousePos = stage.getPointerPosition();
        const containerRect = stage.container().getBoundingClientRect();
        
        tooltip.innerHTML = `
            Seats: ${table.seats}<br>
            Guests: ${table.guests}<br>
            Assigned waiter: ${table.waiter}<br>
            Status: ${table.status}<br>
            Timer: ${hrs}:${mins}:${secs}<br>
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
                    <option value="available" ${table.status === 'available' ? 'selected' : ''}>Available</option>
                    <option value="occupied" ${table.status === 'occupied' ? 'selected' : ''}>Occupied</option>
                    <option value="reserved" ${table.status === 'reserved' ? 'selected' : ''}>Reserved</option>
                </select>
            </div>
            <div class="form-group">
                <label>Number of Guests:</label>
                <input type="number" id="table-guests" value="${table.guests}" min="0" max="${table.seats}">
            </div>
            <div class="form-group">
                <label>Assigned Waiter:</label>
                <input type="text" id="table-waiter" value="${table.waiter}">
            </div>
            <div class="form-group">
                <button onclick="updateTable(${table.id})">Update Table</button>
                <button class="cancel" onclick="cancelEdit()">Cancel</button>
            </div>
            <div class="form-group">
                <button onclick="startTimer()">Start Timer</button> 
                <button class="cancel" onclick="resetTimer()">Reset Timer</button>            
            </div>
        `;
    }

    // Global functions for the editor

    // variables for the timer
    let secs = '00';
    let mins = '00';
    let hrs = '00';
    let millisecs = '00';
    let elaspedTime = 0;
    let timer = null;
    let startTime = 0;
    let isRunning = false;

    
    window.startTimer = function() {

        if(!isRunning){
            startTime = Date.now() - elaspedTime;
            timer = setInterval(updateTimer,10); // update timer every 10 milliseconds
            isRunning = true;
        }
    }

    window.updateTimer = function () {

        const currentTime = Date.now();
        elaspedTime = currentTime - startTime;

        hrs = Math.floor(elaspedTime / (1000 * 60 * 60))
        mins = Math.floor(elaspedTime / (1000 * 60) % 60);
        secs = Math.floor(elaspedTime / 1000 % 60); // Math module to round the number and not get a decimal
        millisecs = Math.floor(elaspedTime % 1000 /10);

        hrs = String(hrs).padStart(2,"0"); // will make the hrs appear with two digits => 00:00:00
        mins = String(mins).padStart(2,"0");
        secs = String(secs).padStart(2,"0");
        millisecs = String(millisecs).padStart(2,"0");

        // tooltip.innerHTML = `${hrs}:${mins}:${secs}`;

    }

    window.resetTimer = function() {

        clearInterval(timer);
        elaspedTime = 0;
        startTime = 0;
        isRunning = false;
        secs = '00';
        mins = '00';
        hrs = '00';
        millisecs = '00';

        // tooltip.innerHTML = '00:00:00';
    }


    window.updateTable = function(tableId) {
        const table = tables.find(t => t.id === tableId);
        if (!table) return;

        // Update table data
        table.status = document.getElementById('table-status').value;
        table.guests = parseInt(document.getElementById('table-guests').value);
        table.waiter = document.getElementById('table-waiter').value;

        // Update shape color
        const shape = selectedShape;
        if (shape) {
            shape.fill(table.status === 'occupied' ? '#dc2626' : 
                      table.status === 'reserved' ? '#f59e0b' : '#22c55e');
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
        const isOccupied = table.status === 'occupied';
        const isReserved = table.status === 'reserved';
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