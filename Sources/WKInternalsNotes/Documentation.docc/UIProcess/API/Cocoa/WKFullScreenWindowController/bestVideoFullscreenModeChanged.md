# ``WKInternalsNotes/WKFullScreenWindowController/bestVideoFullscreenModeChanged()``

visionOS で最適な動画フルスクリーンモードが変わった際、オーナメント表示と親ウィンドウ状態を復帰する。

## Objective-C Declaration
```objective-c
- (void)bestVideoFullscreenModeChanged;
```

## Discussion
`_shouldShowOrnaments` が `false` の場合は何もしない。表示対象の場合はオーナメントをフェード表示した後、親ウィンドウの chrome オプションやリサイズ挙動、最小サイズを復帰し、`_lastKnownParentWindow` と `_parentWindowState`、ベスト動画のインターフェース参照をクリアする。

## References
- [`WKFullScreenWindowControllerIOS.mm#L2197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2197)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
