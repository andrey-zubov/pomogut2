export default class ArticleAccordeon{
    constructor(){
        this.init();
    }

    scrollTo(position){
        $('body, html').animate({scrollTop: position}, 400);
    }

    checkAnchor(){
        const anchor = window.location.hash;
        if (!anchor) return;
        window.scrollTo(0,0);
        history.pushState("", document.title, window.location.pathname);
        const targetBlock = document.querySelector(anchor);
        console.log(targetBlock, anchor);
        if(!targetBlock) return;

        const position = window.innerWidth > 992 ? document.querySelector('.header').getBoundingClientRect().height : 0;
        const endPosition = targetBlock.offsetTop;
        
        this.scrollTo(endPosition);
    }

    bindClick(){
        const anchors = Array.from(document.querySelectorAll('a[href*="#"]'));

        anchors.forEach(a=>{
            a.addEventListener('click', (e)=>{
                e.preventDefault();
                e.stopPropagation();
                const link = e.currentTarget;
                const href = link.getAttribute('href');

                if(!href) return;
                const hrefReplace = href.replace('#', '');              
                const targetHref = document.querySelector(`[id="${href}"]`);
                const targetHrefReplace = document.querySelector(`[id="${hrefReplace}"]`);
                const targetBlock = targetHref || targetHrefReplace;

                if(!targetBlock) return;

                const position = window.innerWidth > 992 ? document.querySelector('.header').getBoundingClientRect().height : 0;
                const endPosition = targetBlock.offsetTop;   
                
                this.scrollTo(endPosition);
            })
        })
    }

    init(){
        this.bindClick();
        this.checkAnchor();
    }
}