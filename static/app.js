const URL = "http://127.0.0.1:5000"
    
function list_cupcake(cupcake) {
    return `
        <div class="card col-md-3 mx-1 px-1 py-1" data-id=${cupcake.id}  style="width: 18rem;">
            <img src="${cupcake.image}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${cupcake.flavor}</h5>
                <p class="card-text">Size: ${cupcake.size}
                    <br /> Rating: ${cupcake.rating}
                </p>
            </div>
            <button class="btn btn-danger btn-sm delete_button"> Remove </button>
        </div>
    `
}

// Handles Initial Display 
async function display() {
    response = await axios.get(`${URL}/api/cupcakes`)
    for (let cupcake of response.data.cupcakes){
        let new_cupcake = list_cupcake(cupcake)
        $('#cupcake_list').prepend(new_cupcake);
    }
}

//Handles Adding of New Cupcake

$('#add_cupake').on('submit', async (evt) => {
    evt.preventDefault();
    let flavor = $('#flavor').val();
    let rating = $('#rating').val();
    let size = $('#size').val();
    let image = $('#image').val();

    let response = await axios.post(`${URL}/api/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });
    let new_cupcake = list_cupcake(response.data.cupcake)
    $('#cupcake_list').prepend(new_cupcake);
    $('#add_cupcake').trigger('reset');
});


//Handles deleting of cupcake

$('#cupcake_list').on('click', '.delete_button', async (evt) => {
    evt.preventDefault();
    let $cupcake = $(evt.target).parent();
    let cupcake_id = $cupcake.attr('data-id');
    await axios.delete(`${URL}/api/cupcakes/${cupcake_id}`);
    $cupcake.remove();
})

display();