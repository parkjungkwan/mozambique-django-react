import React from 'react';
import Header from './Header';
import Footer from './Footer';
import Navbar from './Navbar'


export default function Layout({ children  }: any) {
  return (
    <>
      <Header />
      <Navbar />
      <main>{children}</main>
      <Footer />
    </>
  )
}
  
