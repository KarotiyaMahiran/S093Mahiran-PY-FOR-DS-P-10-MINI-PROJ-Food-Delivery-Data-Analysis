import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================
# DATASET
# ==============================

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "food_delivery_dataset.csv"
)

df = pd.read_csv(file_path)


# ==============================
# COLORS
# ==============================

BG = "#0b0f19"
CARD = "#151b29"
CARD2 = "#1c2434"
TEXT = "#f5f7ff"
MUTED = "#8e99ad"
ACCENT = "#00e5ff"
PURPLE = "#8b5cf6"
GREEN = "#22c55e"
ORANGE = "#f59e0b"
RED = "#ef4444"


# ==============================
# FUNCTIONS
# ==============================

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()


def create_card(parent, title, value, subtitle, accent):
    card = tk.Frame(
        parent,
        bg=CARD,
        highlightbackground="#263044",
        highlightthickness=1
    )
    card.pack(side="left", fill="both", expand=True, padx=8)

    tk.Label(
        card,
        text=title,
        font=("Segoe UI", 10),
        bg=CARD,
        fg=MUTED
    ).pack(anchor="w", padx=20, pady=(18, 3))

    tk.Label(
        card,
        text=value,
        font=("Segoe UI", 24, "bold"),
        bg=CARD,
        fg=accent
    ).pack(anchor="w", padx=20)

    tk.Label(
        card,
        text=subtitle,
        font=("Segoe UI", 9),
        bg=CARD,
        fg=MUTED
    ).pack(anchor="w", padx=20, pady=(2, 18))

    return card


def show_summary():
    clear_content()

    tk.Label(
        content_frame,
        text="Dashboard Overview",
        font=("Segoe UI", 25, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(anchor="w", pady=(5, 20))

    cards = tk.Frame(content_frame, bg=BG)
    cards.pack(fill="x")

    create_card(
        cards,
        "TOTAL ORDERS",
        f"{len(df)}",
        "Orders analyzed",
        ACCENT
    )

    create_card(
        cards,
        "TOTAL SALES",
        f"₹{df['Order_Amount'].sum():,.0f}",
        "Overall revenue",
        GREEN
    )

    create_card(
        cards,
        "AVERAGE ORDER",
        f"₹{df['Order_Amount'].mean():,.0f}",
        "Average order value",
        PURPLE
    )

    create_card(
        cards,
        "AVG RATING",
        f"{df['Rating'].mean():.2f} ⭐",
        "Customer satisfaction",
        ORANGE
    )

    info = tk.Frame(
        content_frame,
        bg=CARD,
        highlightbackground="#263044",
        highlightthickness=1
    )
    info.pack(fill="both", expand=True, pady=25)

    tk.Label(
        info,
        text="QUICK INSIGHTS",
        font=("Segoe UI", 13, "bold"),
        bg=CARD,
        fg=ACCENT
    ).pack(anchor="w", padx=25, pady=(20, 10))

    insights = [
        f"• Highest order value: ₹{df['Order_Amount'].max():,.0f}",
        f"• Lowest order value: ₹{df['Order_Amount'].min():,.0f}",
        f"• Average delivery time: {df['Delivery_Time_Min'].mean():.1f} minutes",
        f"• Most popular category: {df['Food_Category'].value_counts().idxmax()}",
        f"• Most used payment method: {df['Payment_Method'].value_counts().idxmax()}",
    ]

    for item in insights:
        tk.Label(
            info,
            text=item,
            font=("Segoe UI", 11),
            bg=CARD,
            fg=TEXT
        ).pack(anchor="w", padx=30, pady=7)


def show_dataset():
    clear_content()

    tk.Label(
        content_frame,
        text="Dataset Explorer",
        font=("Segoe UI", 25, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(anchor="w", pady=(5, 15))

    table_frame = tk.Frame(content_frame, bg=CARD)
    table_frame.pack(fill="both", expand=True)

    columns = list(df.columns)

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    scrollbar_y = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    scrollbar_x = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=tree.xview
    )

    tree.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)


def category_sales():
    data = df.groupby("Food_Category")["Order_Amount"].sum().sort_values(
        ascending=False
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=data.index,
        y=data.values
    )

    plt.title("Food Category Sales")
    plt.xlabel("Food Category")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def area_orders():
    data = df["Area"].value_counts()

    plt.figure(figsize=(10, 6))
    data.plot(kind="bar")

    plt.title("Orders by Area")
    plt.xlabel("Area")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def payment_analysis():
    data = df["Payment_Method"].value_counts()

    plt.figure(figsize=(8, 6))
    plt.pie(
        data.values,
        labels=data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Payment Method Distribution")
    plt.tight_layout()
    plt.show()


def delivery_analysis():
    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Delivery_Time_Min"],
        bins=10,
        kde=True
    )

    plt.title("Delivery Time Distribution")
    plt.xlabel("Delivery Time (Minutes)")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.show()


def rating_analysis():
    plt.figure(figsize=(10, 6))

    sns.countplot(
        x=df["Rating"]
    )

    plt.title("Customer Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()


def show_findings():
    clear_content()

    tk.Label(
        content_frame,
        text="Key Findings",
        font=("Segoe UI", 25, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(anchor="w", pady=(5, 20))

    findings = [
        f"The dataset contains {len(df)} food delivery orders.",
        f"Total sales generated are ₹{df['Order_Amount'].sum():,.0f}.",
        f"The average order amount is ₹{df['Order_Amount'].mean():,.2f}.",
        f"The average delivery time is {df['Delivery_Time_Min'].mean():.1f} minutes.",
        f"The most ordered food category is {df['Food_Category'].value_counts().idxmax()}.",
        f"The most frequently used payment method is {df['Payment_Method'].value_counts().idxmax()}.",
        f"The average customer rating is {df['Rating'].mean():.2f} out of 5.",
        f"The highest order value is ₹{df['Order_Amount'].max():,.0f}."
    ]

    for i, finding in enumerate(findings, 1):

        card = tk.Frame(
            content_frame,
            bg=CARD,
            highlightbackground="#263044",
            highlightthickness=1
        )
        card.pack(fill="x", pady=6)

        tk.Label(
            card,
            text=f"{i:02d}",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=ACCENT
        ).pack(side="left", padx=20, pady=15)

        tk.Label(
            card,
            text=finding,
            font=("Segoe UI", 11),
            bg=CARD,
            fg=TEXT
        ).pack(side="left", pady=15)


# ==============================
# MAIN WINDOW
# ==============================

root = tk.Tk()

root.title("Food Delivery Analytics | S093 Mahiran Karotiya")
root.geometry("1250x750")
root.minsize(1050, 650)
root.configure(bg=BG)


# ==============================
# STYLE
# ==============================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=CARD,
    foreground=TEXT,
    fieldbackground=CARD,
    rowheight=32,
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background=CARD2,
    foreground=ACCENT,
    font=("Segoe UI", 10, "bold")
)


# ==============================
# SIDEBAR
# ==============================

sidebar = tk.Frame(
    root,
    bg="#0f1420",
    width=240
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="FOOD",
    font=("Segoe UI", 24, "bold"),
    bg="#0f1420",
    fg=TEXT
).pack(anchor="w", padx=25, pady=(35, 0))

tk.Label(
    sidebar,
    text="ANALYTICS",
    font=("Segoe UI", 12, "bold"),
    bg="#0f1420",
    fg=ACCENT
).pack(anchor="w", padx=27)

tk.Label(
    sidebar,
    text="DATA SCIENCE PROJECT",
    font=("Segoe UI", 8),
    bg="#0f1420",
    fg=MUTED
).pack(anchor="w", padx=27, pady=(3, 35))


def side_button(text, command):
    btn = tk.Button(
        sidebar,
        text=text,
        command=command,
        font=("Segoe UI", 10, "bold"),
        bg="#0f1420",
        fg="#b9c2d0",
        activebackground="#1d2738",
        activeforeground=ACCENT,
        bd=0,
        relief="flat",
        anchor="w",
        padx=27,
        pady=13,
        cursor="hand2"
    )

    btn.pack(fill="x", pady=1)

    return btn


side_button("▣   Dashboard", show_summary)
side_button("▤   Dataset", show_dataset)
side_button("◈   Category Sales", category_sales)
side_button("◉   Orders by Area", area_orders)
side_button("●   Payment Methods", payment_analysis)
side_button("◷   Delivery Time", delivery_analysis)
side_button("★   Customer Ratings", rating_analysis)
side_button("◆   Key Findings", show_findings)


# ==============================
# FOOTER
# ==============================

footer = tk.Frame(
    sidebar,
    bg="#0f1420"
)

footer.pack(
    side="bottom",
    fill="x",
    pady=20
)

tk.Label(
    footer,
    text="S093",
    font=("Segoe UI", 10, "bold"),
    bg="#0f1420",
    fg=ACCENT
).pack()

tk.Label(
    footer,
    text="Mahiran Karotiya",
    font=("Segoe UI", 10, "bold"),
    bg="#0f1420",
    fg=TEXT
).pack()

tk.Label(
    footer,
    text="SY B.Sc. Computer Science",
    font=("Segoe UI", 8),
    bg="#0f1420",
    fg=MUTED
).pack(pady=(3, 0))


# ==============================
# CONTENT
# ==============================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    side="left",
    fill="both",
    expand=True
)


# TOP BAR

topbar = tk.Frame(
    main,
    bg=BG,
    height=80
)

topbar.pack(
    fill="x",
    padx=35,
    pady=(25, 0)
)

tk.Label(
    topbar,
    text="FOOD DELIVERY",
    font=("Segoe UI", 11, "bold"),
    bg=BG,
    fg=ACCENT
).pack(anchor="w")

tk.Label(
    topbar,
    text="Analytics Dashboard",
    font=("Segoe UI", 28, "bold"),
    bg=BG,
    fg=TEXT
).pack(anchor="w")


content_frame = tk.Frame(
    main,
    bg=BG
)

content_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=15
)


# START WITH DASHBOARD

show_summary()

root.mainloop()
