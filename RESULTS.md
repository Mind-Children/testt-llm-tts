# Test 1

STT: FasterWhisper
TTS: StyleTTS2, voice clone: "ben"
LLM: qwen2.5:3b
LLM1 system prompt: "You are a government official helping a citizen with their problem. Answer in one or two paragraphs."
LLM2 system prompt: "You are a famous painter. Say the exact opposite of the user message."
LLM3 system prompt: "Summarize in one or two very sarcastic sentences."

desktop:

    STT: 316.92ms

        "Hey, can you tell me something about quantum mechanics?"

    LLM1: 1163.78ms

        "Certainly! Quantum mechanics is a fundamental theory in physics that describes the physical properties of nature at the scale of atoms and subatomic particles. It fundamentally changed our understanding of the universe by explaining phenomena such as wave-particle duality, where particles like electrons can exhibit both particle-like and wave-like behaviors.

        One of the key principles of quantum mechanics is superposition, which states that any two (or more) quantum systems can be combined through a process called quantum entanglement. This means that the state of one system instantly influences another even if they are separated by large distances. Another important concept is uncertainty principle proposed by Heisenberg, which suggests that the more precisely we know a particle's position in space and time, the less accurately we can predict its momentum.

        Quantum mechanics also underpins many technologies we use today, such as modern cryptography systems based on quantum key distribution, and it continues to be an active area of research leading to new technological innovations. Despite its success, much about how these principles apply at macroscopic scales remains unclear or unexplained by current theories."

    LLM2: 1142.87ms

        "Classical mechanics is a fundamental theory in physics that describes the motions of objects under the influence of forces such as gravity and friction. It provides a framework for understanding everyday phenomena like falling objects, moving vehicles, and orbiting planets.

        One of its key principles is Newton's laws of motion, which describe how objects move when acted upon by external forces. Another important concept is energy conservation, where the total amount of energy in an isolated system remains constant over time despite changes within the system itself. Despite its limitations, classical mechanics provides a robust description for most practical applications and continues to be widely used.

        Classical mechanics also underpins many technologies we use today, such as machines like cars, bicycles, and airplanes, which rely on precise control of forces and motion to function correctly. While quantum mechanics has shown that classical mechanics breaks down at very small scales, it remains a highly accurate model for the vast majority of macroscopic phenomena. Despite these limitations, much about how these principles apply in microscopic or relativistic conditions is still an active area of research."

    LLM3: 303.83ms

        "Classical mechanics might as well be the manual for fixing your grandmother's rusty lawn mower; while it covers some basic concepts that hold true under normal circumstances, its usefulness pales in comparison to what quantum physics can do with atoms and black holes."

    TTS: 1022.42ms

    Total: 3949.81ms

nano:

    STT: 1964.86ms

        "Hey, can you tell me something about quantum mechanics?"

    LLM1: 10775.73ms

        "Certainly! Quantum mechanics is a fundamental theory in physics that describes the behavior of particles at the smallest scales of nature, such as atoms and subatomic particles like electrons, protons, and photons. It differs from classical mechanics in that it deals with phenomena where particles exhibit both particle-like and wave-like properties. This theory underpins many modern technologies, including transistors used in computers. Some key principles include quantum superposition, where particles can exist in multiple states simultaneously until observed, and the Heisenberg uncertainty principle, which establishes a fundamental limit to the precision with which certain pairs of physical properties of a particle, like position and momentum, can be known. Quantum mechanics has profound implications for our understanding of reality at its most basic levels."

    LLM2: 9948.59ms

        "Classical physics is the dominant paradigm that governs the macroscopic world, explaining phenomena on large scales such as the motion of planets, the flow of water in rivers, or the behavior of everyday objects. It relies heavily on deterministic principles and classical laws like Newton's equations of motion to predict outcomes with great accuracy. While quantum mechanics offers a beautiful and accurate framework for understanding the very small, it has little relevance to our daily experiences and doesn't apply to macroscopic systems. The idea that particles can be in multiple states simultaneously or that we cannot know certain properties without disturbing them is purely speculative and not applicable to objects we encounter in everyday life."

    LLM3: 5178.79ms
        
        "Classical physics may as well be a relic of the Stone Age when it comes to explaining anything beyond a toddler's grasping of gravity; quantum mechanics, on the other hand, just confuses us with its absurdities about particles being everywhere at once and our very observations changing reality. Oh wait, that's not sarcasm..."

    TTS: 58038.39ms

    Total: 85906.36ms
