import React from 'react';
import {NavLink} from 'react-router-dom';

import classes from './Nav.module.css'

const navbar = () => {
    return (
        <nav  className={[classes.Navbar,"navbar","navbar-expand-lg","navbar-dark"].join(' ')}>
            <div  className="container-fluid">
                <a  className="navbar-brand" href="/">Tok Task</a>
                <button  className={[classes.Button,"navbar-toggler"].join(' ')} type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span  className="navbar-toggler-icon"></span>
                </button>
                <div  className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul  className="navbar-nav mb-2 mb-lg-0">
                        <li  className="nav-item">
                            <NavLink className="nav-link" to="/" activeClassName={classes.Active}>Home </NavLink>
                        </li>
                        <li  className="nav-item">
                             <NavLink className="nav-link" to="/posts" activeClassName={classes.Active}>News</NavLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}


export default navbar;