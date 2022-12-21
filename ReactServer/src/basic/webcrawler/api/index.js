import {server, webcrawler} from 'context'
const webcrawlerService = {
    naverMovie
}
function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}
async function naverMovie(){
    fetch(`${server}${webcrawler}naver-movie`)
    .then(handleResponse)
    .then(data => {
        alert('1위영화 >>> '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
    
}
export default webcrawlerService