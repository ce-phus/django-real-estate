import React from 'react'
import { Container, Nav, Navbar, NavDropdown } from "react-bootstrap"
import { FaSignInAlt, FaSignOutAlt } from "react-icons/fa"
import { GiHouse } from "react-icons/gi"
import { useDispatch, useSelector } from "react-redux"
import { LinkContainer } from "react-router-bootstrap";
import { useNavigate } from "react-router-dom"
import { logout, reset } from "../features/auth/authSlice"

const Header = () => {
  return (
    <div>Header</div>
  )
}

export default Header