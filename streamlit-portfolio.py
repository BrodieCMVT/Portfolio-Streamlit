import streamlit as st

with st.container(border=True,height=None):
    st.header('Brodies Portfolio')

    index, page1, page2, page3, page4, resume = st.tabs(['Index','HTML Projects','PHP Projects','Word Documents','Powerpoints','Resume'])
    with index:
        st.subheader('Hobbies')
        st.text('Computer Programming\nWebsite Building\nDisc Golf\nRacket Ball\nPlaying Games')
        st.subheader('Occupations')
        st.text('Columbia Montour Vo-Tech Senior\nSales Associate:Riteaid')
        st.subheader('Skills')
        st.text('Knowlege in multiple programming languages\nProblem Solving\nCooperative\nMotivated')

    with page1:
        st.link_button('PC Store','http://areawebsites.org/bForce/10th-pc-store/index.html')
        st.link_button('DJ Turntable','http://areawebsites.org/bForce/DJ_Turntable/index.html')
        st.link_button('Park Website','http://areawebsites.org/bForce/Park/index.html')
        st.link_button('Site Portal','http://areawebsites.org/bForce/portal/portal.html')
        st.link_button('Mobile','http://areawebsites.org/bForce/moble/mport.html')
        st.link_button('Joe Plumber','http://areawebsites.org/bForce/Joe/index.html')
        st.link_button('Laptop Shop','http://areawebsites.org/bForce/laptops/index.html')

    with page2:
        st.link_button('Payroll Calculator','http://areawebsites.org/bForce/payroll/paycalc.php')
        st.link_button('Web Builder','http://areawebsites.org/bForce/webbuild/webbuild.html')
        st.link_button('Burger Ordering','http://areawebsites.org/bForce/burger/burger.php')
        st.link_button('PHP Loops','http://areawebsites.org/bForce/phploop/loophp.php')
        st.link_button('Gas Increase Calc','http://areawebsites.org/bForce/gasphp/gas.php')
        st.link_button('Pampered Pups Site','http://areawebsites.org/bForce/Pampered_Pups/index.php')
        st.link_button('Computer Games Database','http://areawebsites.org/bForce/PHPCG/CGH.php')
        st.link_button('PC Survey','http://areawebsites.org/bForce/CTsurvey/index.php')
        st.link_button('Dashboard','http://areawebsites.org/bForce/Dashboard/dash.php')
        st.link_button('E-Estates','http://areawebsites.org/bForce/realestate/index.php')

    with page3:
        st.link_button('Dream Job News','http://areawebsites.org/bForce/w1.pdf')
        st.link_button('Tutorial','http://areawebsites.org/bForce/w2.pdf')
        st.link_button('Comp Jobs','http://areawebsites.org/bForce/w3.pdf')
        st.link_button('Occupation Research','http://areawebsites.org/bForce/sqa.pdf')

    with page4:
        st.link_button('Skateboards Inc.','http://areawebsites.org/bForce/skate.pdf')
        st.link_button('How-To','http://areawebsites.org/bForce/How-to.pdf')
        st.link_button('CIS Overview','http://areawebsites.org/bForce/Computer%20Information%20Systems.pdf')

    with resume:
        st.image('Brodie Force - Resume 2024 updated.png')
        with open("Brodie Force - Resume 2024 updated.pdf", "rb") as file:
            st.download_button(label="Download PDF",file_name='Brodie Force - Resume 2024 updated.pdf',data=file)