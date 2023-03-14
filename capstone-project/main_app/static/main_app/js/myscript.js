

$('.plus-cart').onClick(function(){
    let id=$(this).attr("pid").toString();
    let eml = this.parentNode.children[2]
    console.log("pid =", id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data = ", data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innnerText=data.totalamount
        }
    })
})


$('.minus-cart').click(function(){
  let id=$(this).attr("pid").toString();
  let eml = this.parentNode.children[2]
  $.ajax({
      type:"GET",
      url:"/minuscart",
      data:{
          prod_id:id
      },
      success:function(data){
          eml.innerText=data.quantity
          document.getElementById("amount").innerText=data.amount
          document.getElementById("totalamount").innnerText=data.totalamount
      }
  })
})

$('.remove-cart').click(function(){
  let id=$(this).attr("pid").toString();
  var eml=this
  $.ajax({
      type:"GET",
      url:"/removecart",
      data:{
          prod_id:id
      },
      success:function(data){
          document.getElementById("amount").innerText=data.amount
          document.getElementById("totalamount").innnerText=data.totalamount
          eml.parentNode.parentNode.parentNode.parentNode.remove()
      }
  })
})