#    This is a component of emc2
#    Copyright 2007 Jeff Epler <jepler@unpythonic.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys
import tkinter

def properties(app, title, names, props):
    t = tkinter.Toplevel(app)
    t.wm_transient(app)
    t.wm_title(title)
    t.wm_iconname(title)
    t.wm_resizable(0,0)
     
    for i, (k, n) in enumerate(names):
        if k not in props: continue
        l = tkinter.Label(t, text = n)
        l.grid(row=i, column=0, sticky="nw")
        l = tkinter.Label(t, text = props[k], wraplength=200, justify="l")
        l.grid(row=i, column=1, sticky="nw")
    
    b = tkinter.Button(t, text=_("OK"), command=t.destroy, default="active", padx=0, pady=0, width=10)
    b.grid(row=i+1, column=0, columnspan=2) 
    t.after_idle(b.focus)
    t.bind("<Escape>", lambda e: t.destroy()) 
    t.bind("<Return>", lambda e: t.destroy()) 
    return t


