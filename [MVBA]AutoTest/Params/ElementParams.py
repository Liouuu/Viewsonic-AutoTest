from enum import Enum


class c_ElementParam:
    @property
    def _Site(self): return "com.viewsonic.droid"
    @property
    def _Id_titleTextView(self): return self._Site+":id/titleTextView"
    @property
    def _Id_btnLasso(self): return self._Site+":id/btnLasso"
    @property
    def _Id_btnFile(self): return self._Site+":id/btnFile"
    @property
    def _Id_btnTypingText(self): return self._Site+":id/btnTypingText"
    @property
    def _Id_spinnerFontName(self): return self._Site+":id/spinnerFontName"
    @property
    def _Id_spinnerFontSize(self): return self._Site+":id/spinnerFontSize"
    @property
    def _Id_editText(self): return self._Site+":id/editText"
    @property
    def _Id_buttonDelete(self): return self._Site+":id/buttonDelete"
    @property
    def _Id_buttonMenuClose(self): return self._Site+":id/buttonMenuClose"
    @property
    def _Id_buttonLocked(self): return self._Site+":id/buttonLocked"
    @property
    def _Id_buttonHyperlink(self): return self._Site+":id/buttonHyperlink"
    @property
    def _Id_buttonCopy(self): return self._Site+":id/buttonCopy"
    @property
    def _Id_buttonCut(self): return self._Site+":id/buttonCut"
    @property
    def _Id_buttonReplicate(self): return self._Site+":id/buttonReplicate"
    @property
    def _Id_buttonMoveLayer(self): return self._Site+":id/buttonMoveLayer"
    @property
    def _Id_buttonFlip(self): return self._Site+":id/buttonFlip"
    @property
    def _Id_buttonMirror(self): return self._Site+":id/buttonMirror"

    @property
    def _Id_buttonSaveResource(
        self): return self._Site+":id/buttonSaveResource"

    @property
    def _Id_buttonCrop(self): return self._Site+":id/buttonCrop"
    @property
    def _Id_buttonFitToScreen(self): return self._Site+":id/buttonFitToScreen"

    @property
    def _Id_buttonSetAsBackground(
        self): return self._Site+":id/buttonSetAsBackground"

    @property
    def _Id_buttonStrokeWidth(self): return self._Site+":id/buttonStrokeWidth"

    @property
    def _Id_seekBarStrokeWidth(
        self): return self._Site+":id/seekBarStrokeWidth"

    @property
    def _Id_buttonColor(self): return self._Site+":id/buttonColor"
    @property
    def _Id_buttonFill(self): return self._Site+":id/buttonFill"
    @property
    def _Id_buttonSnapshot(self): return self._Site+":id/buttonSnapshot"
    @property
    def _Id_buttonAlpha(self): return self._Site+":id/buttonAlpha"
    @property
    def _Id_seekBarAlpha(self): return self._Site+":id/seekBarAlpha"
    @property
    def _Id_btnBackground(self): return self._Site+":id/btnBackground"
    @property
    def _Id_radioColor(self): return self._Site+":id/radioColor"
    @property
    def _Id_radioBuiltin(self): return self._Site+":id/radioBuiltin"

    @property
    def _Id_radioOriginalContent(
        self): return self._Site+":id/radioOriginalContent"

    @property
    def _Id_radioLocalBG(self): return self._Site+":id/radioLocalBG"
    @property
    def _Id_radioFollowMeBG(self): return self._Site+":id/radioFollowMeBG"
    @property
    def _Id_buttonNeutral(self): return self._Site+":id/buttonNeutral"
    @property
    def _Id_buttonCancel(self): return self._Site+":id/buttonCancel"
    @property
    def _Id_checkGridLine(self): return self._Site+":id/checkGridLine"
    @property
    def _Id_checkWaterMark(self): return self._Site+":id/checkWaterMark"
    @property
    def _Id_buttonStandard(self): return self._Site+":id/buttonStandard"
    @property
    def _Id_buttonAdvanced(self): return self._Site+":id/buttonAdvanced"
    @property
    def _Id_btnEraser(self): return self._Site+":id/btnEraser"

    @property
    def _Id_buttonEraseSelector(
        self): return self._Site+":id/buttonEraseSelector"

    @property
    def _Id_buttonEraseAll(self): return self._Site+":id/buttonEraseAll"

    @property
    def _Id_btnSubEraserEraser(
        self): return self._Site+":id/btnSubEraserEraser"

    @property
    def _Id_btnSubEraserSelector(
        self): return self._Site+":id/btnSubEraserSelector"

    @property
    def _Id_btnSubEraserEraserAll(
        self): return self._Site+":id/btnSubEraserEraserAll"

    @property
    def _Id_seekBar(self): return self._Site+":id/seekBar"
    @property
    def _Id_radioFileOpen(self): return self._Site+":id/radioFileOpen"
    @property
    def _Id_btnPaste(self): return self._Site+":id/btnPaste"
    @property
    def _Id_btnPageAdd(self): return self._Site+":id/btnPageAdd"
    @property
    def _Id_btnPageNext(self): return self._Site+":id/btnPageNext"
    @property
    def _Id_btnPagePrev(self): return self._Site+":id/btnPagePrev"
    @property
    def _Id_searchEditText(self): return self._Site+":id/searchEditText"
    @property
    def _Id_search_icon(self): return self._Site+":id/search_icon"

    @property
    def _Id_textSaveResourceFormat(
        self): return self._Site+":id/textSaveResourceFormat"

    @property
    def _Id_textActivate(self): return self._Site+":id/textActivate"
    @property
    def _Id_buttonPersonal(self): return self._Site+":id/buttonPersonal"
    @property
    def _Id_editName(self): return self._Site+":id/editName"
    @property
    def _Id_editEmail(self): return self._Site+":id/editEmail"
    @property
    def _Id_editEmailC(self): return self._Site+":id/editEmailC"
    @property
    def _Id_buttonSubmit(self): return self._Site+":id/buttonSubmit"
    @property
    def _Id_buttonOk(self): return self._Site+":id/buttonOk"
    @property
    def _Id_editSignInEmail(self): return self._Site+":id/editSignInEmail"

    @property
    def _Id_editSignInPassword(
        self): return self._Site+":id/editSignInPassword"

    @property
    def _Id_btnResource(self): return self._Site+":id/btnResource"
    @property
    def _Id_currentFolder(self): return self._Site+":id/currentFolder"
    @property
    def _Id_radioLocalStorage(self): return self._Site+":id/radioLocalStorage"
    @property
    def _Id_radioGoogleDrive(self): return self._Site+":id/radioGoogleDrive"
    @property
    def _Id_radioOneDrive(self): return self._Site+":id/radioOneDrive"

    @property
    def _Id_radioOneDriveBusiness(
        self): return self._Site+":id/radioOneDriveBusiness"

    @property
    def _Id_radioDropBox(self): return self._Site+":id/radioDropBox"
    @property
    def _Id_radioBox(self): return self._Site+":id/radioBox"
    @property
    def _Id_radioImage(self): return self._Site+":id/radioImage"
    @property
    def _Id_radioVideo(self): return self._Site+":id/radioVideo"
    @property
    def _Id_radioAudio(self): return self._Site+":id/radioAudio"
    @property
    def _Id_radioImageSearch(self): return self._Site+":id/radioImageSearch"
    @property
    def _Id_parentTitleBar(self): return self._Site+":id/parentTitleBar"

    @property
    def _Id_sticky_note_canvas_layout(
        self): return self._Site+":id/sticky_note_canvas_layout"

    @property
    def _Id_titleBar(self): return self._Site+":id/titleBar"
    @property
    def _Id_layoutControlBar(self): return self._Site+":id/layoutControlBar"
    @property
    def _Id_layoutAdorner(self): return self._Site+":id/layoutAdorner"
    @property
    def _Id_btnShape(self): return self._Site+":id/btnShape"
    @property
    def _Id_radioShape(self): return self._Site+":id/radioShape"

    @property
    def _Id_radioPseudo3DShape(
        self): return self._Site+":id/radioPseudo3DShape"

    @property
    def _Id_radioLines(self): return self._Site+":id/radioLines"
    @property
    def _Id_seekBarWidth(self): return self._Site+":id/seekBarWidth"
    @property
    def _Id_radioSticky(self): return self._Site+":id/radioSticky"
    @property
    def _Id_buttonTypingText(self): return self._Site+":id/buttonTypingText"
    @property
    def _Id_buttonPen(self): return self._Site+":id/buttonPen"
    @property
    def _Id_checkItalic(self): return self._Site+":id/checkItalic"
    @property
    def _Id_checkUnderline(self): return self._Site+":id/checkUnderline"

    @property
    def _Id_sticky_note_canvas(
        self): return self._Site+":id/sticky_note_canvas"

    @property
    def _Id_drawColor(self): return self._Site+":id/drawColor"

    @property
    def _Id_seekBarWidthHighlighter(
        self): return self._Site+":id/seekBarWidthHighlighter"

    @property
    def _Id_buttonColorBg(self): return self._Site+":id/buttonColorBg"
    @property
    def _Id_checkUpscript(self): return self._Site+":id/checkUpscript"
    @property
    def _Id_checkDownscript(self): return self._Site+":id/checkDownscript"
    @property
    def _Id_checkAlignLeft(self): return self._Site+":id/checkAlignLeft"
    @property
    def _Id_checkAlignRight(self): return self._Site+":id/checkAlignRight"
    @property
    def _Id_checkAlignCenter(self): return self._Site+":id/checkAlignCenter"
    @property
    def _Id_checkBulleted(self): return self._Site+":id/checkBulleted"
    @property
    def _Id_buttonIncIndent(self): return self._Site+":id/buttonIncIndent"
    @property
    def _Id_buttonDecIndent(self): return self._Site+":id/buttonDecIndent"

    @property
    def _Id_capture_menu_buttonMenuClose(
        self): return self._Site+":id/capture_menu_buttonMenuClose"

    @property
    def _Id_title(self): return self._Site+":id/title"
    @property
    def _Id_btnMeeting(self): return self._Site+":id/btnMeeting"
    @property
    def _Id_connect_cast(self): return self._Site+":id/connect_cast"
    @property
    def _Id_btnCapture(self): return self._Site+":id/btnCapture"

    @property
    def _Id_capture_menu_button_capture(
        self): return self._Site+":id/capture_menu_button_capture"

    @property
    def _Id_capture_menu_button_capture_rectangle_capture(
        self): return self._Site+":id/capture_menu_button_capture_rectangle_capture"

    @property
    def _Id_capture_menu_button_record(
        self): return self._Site+":id/capture_menu_button_record"

    @property
    def _Id_capture_menu_button_live(
        self): return self._Site+":id/capture_menu_button_live"

    @property
    def _Id_radioFileSave(self): return self._Site+":id/radioFileSave"
    @property
    def _Id_radioFileSaveAs(self): return self._Site+":id/radioFileSaveAs"
    @property
    def _Id_radioFileExport(self): return self._Site+":id/radioFileExport"
    @property
    def _Id_spnFileExportType(self): return self._Site+":id/spnFileExportType"

    @property
    def _Id_editFileExportName(
        self): return self._Site+":id/editFileExportName"

    @property
    def _Id_btnFileExportOK(self): return self._Site+":id/btnFileExportOK"
    @property
    def _Id_buttonFileEmail(self): return self._Site+":id/buttonFileEmail"
    @property
    def _Id_buttonQRCodeFile(self): return self._Site+":id/buttonQRCodeFile"
    @property
    def _Id_radioAIPen(self): return self._Site+":id/radioAIPen"
    @property
    def _Id_radioMathTools(self): return self._Site+":id/radioMathTools"

    @property
    def _Id_radioDocumentCamera(
        self): return self._Site+":id/radioDocumentCamera"

    @property
    def _Id_radioYoutubeSearch(
        self): return self._Site+":id/radioYoutubeSearch"

    @property
    def _Id_radioThrow(self): return self._Site+":id/radioThrow"
    @property
    def _Id_radioClipsSearch(self): return self._Site+":id/radioClipsSearch"
    @property
    def _Id_btnPen(self): return self._Site+":id/btnPen"
    @property
    def _Id_radioPen(self): return self._Site+":id/radioPen"
    @property
    def _Id_radioHighlighter(self): return self._Site+":id/radioHighlighter"
    @property
    def _Id_radioShapePen(self): return self._Site+":id/radioShapePen"
    @property
    def _Id_radioMagicLinePen(self): return self._Site+":id/radioMagicLinePen"
    @property
    def _Id_checkBold(self): return self._Site+":id/checkBold"
    @property
    def _Id_checkItalic(self): return self._Site+":id/checkItalic"
    @property
    def _Id_checkUnderline(self): return self._Site+":id/checkUnderline"
    @property
    def _Id_checkbuttonColor(self): return self._Site+":id/checkbuttonColor"

    @property
    def _Id_checkbuttonColorBg(
        self): return self._Site+":id/checkbuttonColorBg"

    @property
    def _XPath_Canvas(
        self): return "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]"


ElementParam = c_ElementParam()
