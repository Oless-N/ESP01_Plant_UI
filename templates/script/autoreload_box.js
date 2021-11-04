<span>Auto Refresh</span>&nbsp;<input type="checkbox" id="item_id" value="true" checked="checked" />

<script type="text/javascript">
setInterval(function ()
{
    if (document.getElementById("item_id").checked)
    {
        location.reload();
    }
}, 5000); // interval is in milliseconds
</script>


  <script>
        var relay = document.getElementById("setup_but");
        function relay_inverse() {
            var request = new XMLHttpRequest();
            request.open('GET','/relay_switch',false);
            request.send();
        }
        relay.addEventListener('click', relay_inverse);
    </script>