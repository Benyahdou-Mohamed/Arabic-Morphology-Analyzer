# analyzer.py
# Arabic morphology analysis using Qalsadi

from qalsadi.analex import Analex


class MorphologyAnalyzer:
    """Handles Arabic text morphological analysis"""
    
    def __init__(self):
        self.analex = Analex()
    
    @staticmethod
    def normalize_tags(tags):
        """Convert tags to string format"""
        if isinstance(tags, (list, tuple)):
            return ":".join(tags)
        return str(tags or "")
    
    @staticmethod
    def guess_pos(tags, word_type):
        """Guess part of speech from tags"""
        s = MorphologyAnalyzer.normalize_tags(tags)
        if "Verb" in word_type or "فعل" in s:
            return "فعل"
        if "Noun" in word_type or "اسم" in s:
            return "اسم"
        if "Particle" in word_type or "حرف" in s:
            return "حرف"
        return "غير محدد"
    
    @staticmethod
    def guess_i3rab(tags):
        """Guess grammatical case from tags"""
        s = MorphologyAnalyzer.normalize_tags(tags)
        if "مرفوع" in s:
            return "مرفوع"
        if "منصوب" in s:
            return "منصوب"
        if "مجرور" in s:
            return "مجرور"
        if "مجزوم" in s:
            return "مجزوم"
        if "مبني" in s:
            return "مبني"
        return "غير معروف"
    
    @staticmethod
    def guess_gender(tags):
        """Guess gender from tags"""
        s = MorphologyAnalyzer.normalize_tags(tags)
        if "مؤنث" in s:
            return "مؤنث"
        if "مذكر" in s:
            return "مذكر"
        return "غير محدد"
    
    def analyze_text(self, text):
        """
        Analyze Arabic text and return morphological information
        
        Args:
            text: Arabic text to analyze
            
        Returns:
            List of dictionaries containing word analysis
        """
        raw_results = self.analex.check_text(text)
        analyzed_words = []
        
        for item in raw_results:
            # Get best analysis
            best = item[0] if isinstance(item, list) else item
            
            # Extract word and tags
            word = best.get("word") or best.get("token")
            tags = best.get("tags")
            word_type = best.get("type", "")
            
            # Build system analysis
            system_analysis = {
                "pos": self.guess_pos(tags, word_type),
                "i3rab": self.guess_i3rab(tags),
                "gender": self.guess_gender(tags)
            }
            
            # Store result
            analyzed_words.append({
                "mot": word,
                "system": system_analysis,
                "user": None  # Will be filled from database
            })
        
        return analyzed_words