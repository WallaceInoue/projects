let input = document.querySelector('.inptas')
let butt = document.querySelector('.addtask')
let fulllist = document.querySelector('.list')
let mylist = []

function addinput(){
        mylist.push({
            task: input.value,
            ok: false }
        )
        input.value = ''
        showtask()
        
   }
function showtask(){
    
    let newlist = ''
    
    mylist.forEach((tarefa, index) => {
        
        newlist= newlist +`
        
        <li class="task ${tarefa.ok && "done"}">
                <img src="checked.png" alt="check.na.tarefa"onclick="taskok(${index})" >
             <p> ${tarefa.task} </p>
                <img src="trash.png" alt="delete.task" onclick="delet(${index})">
        </li> `
    })
   
   fulllist.innerHTML= newlist
   
   localStorage.setItem('lista', JSON.stringify(mylist))
     }
     function taskok(index){
        mylist[index].ok= !mylist[index].ok
        showtask()
     }

     function delet(index){
        mylist.splice(index, 1)
        showtask()
     }
     function reload(){
        let loca = localStorage.getItem('lista')
        if(loca){
        mylist = JSON.parse(loca)}
        showtask() 
     }
    reload()
   butt.addEventListener('click', addinput)