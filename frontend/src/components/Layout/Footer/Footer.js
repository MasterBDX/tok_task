import React from 'react';

import classes from './Footer.module.css';

const footer = ()=>{
    return <footer className={[classes.Footer,"fixed-bottom"].join(' ')}>  
                <span>
                    Footer
                </span>
           </footer>
}

export default footer;