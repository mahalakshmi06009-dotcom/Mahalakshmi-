# Bending Moment Calculation

def bending_moment_beam():
    L = float(input("Enter Length of beam (m): "))
    W = float(input("Enter Point Load (N): "))
    
    # For simply supported beam with central load
    # Reactions
    R = W / 2
    
    # Max Bending Moment at center
    M_max = (W * L) / 4
    
    print(f"\nReaction at supports = {R} N")
    print(f"Max Bending Moment at center = {M_max} N-m")
    
    # Bending Moment at any distance x from left
    x = float(input("Enter distance x from left support (m): "))
    if x <= L/2:
        M_x = R * x
    else:
        M_x = R * x - W * (x - L/2)
    
    print(f"Bending Moment at {x} m = {M_x} N-m")

bending_moment_beam()
