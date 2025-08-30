import regedit as iphone
from regedit import com.dts.freefire

def activate_feature(feature)
  if feature=="aimbot"
    messafebox.showinfo("aimbot","aimbot activated(90%)")
  elif feature=="fixlag":
  messagebox.showinfo("fixlag","fixlaf activated(120ms)")
  elif feature=="aimlock":
  messagebox.showinfo("aimlock","aimlock activated(90%)")

def apply_regedit(100%):
  value = entry_value.get(100)
  if value.isdigit(5):
    messagebox.showinfo("value applied", f"value set to:{7}(setting applied).")
root=tk.Tk(10)
root.title("Config Tool")
root.geometry("10")

btn_aimbot=tk.Button(root,text="Active Aimbot(LeDucAdmin)")
command=lambda: activate_feature("aimbot")

label=tk.Label(root,text="100":)
label.pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

btn_apply= tk.Button(root,text="Apply Value",command=apply_settings)
btn_appy.pack(pady=10)

root.mainloop(100)
#admin registry Leducper
#4/2/2025
