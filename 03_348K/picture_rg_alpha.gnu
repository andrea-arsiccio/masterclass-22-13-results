set terminal png size 960,960 font arial 30 truecolor butt enhanced
       set output '| display png:-'
set   autoscale                        # scale axes automatically
      unset log                              # remove any log-scaling
      unset label                            # remove any previous labels
      set border linewidth 5
      set xtic 0.6,0.2,1.4 font "Helvetica,40"                         # set xtics automatically
      set ytic 0,2,10 font "Helvetica,40"                         # set ytics automatically
#      set title "Force Deflection Data for a Beam and a Column"
       set xlabel "R_g (nm)" font "Helvetica,40"
       set ylabel "Alpha helix content" font "Helvetica,40"
       unset key 
#      set label "Yield Point" at 0.003,260
#      set arrow from 0.0028,250 to 0.003,280
       set xr [0.6:1.4]
       set yr [0:10]
#       set cbrange [0:2]
       set format x "%4.1f" 
       set pm3d
       set pm3d interpolate 10,10
       set pm3d map
       set format z "%4.1f"
       unset surface
#       set palette defined (0 "white", 0.001 "red", 0.002 "yellow", 0.003 "green", 0.004 "blue", 0.007 "black")
       set palette defined (0 "white", 0.001 "#C0C0C0" , 0.002 "#D2B48C" , 0.004 "#CD5C5C", 0.006 "#00008B", 0.008 "black")
#       set palette defined (0 "white", 0.001 "silver", 0.002 "rosybrown", 0.004 "lightsteelblue", 0.006 "darkblue", 0.008 "black")
  #     set format cb "%2.0f"
       set cbtics font "Helvetica,40"
#       set label "A(18.2%)" at 1.21,2.86 front        
#       set label "B(24.7%)" at 1.69,0.66 front       

set tmargin at screen 0.75
set bmargin at screen 0.2
set rmargin at screen 0.75
set lmargin at screen 0.2     

       splot  "./normFEL.dat"


