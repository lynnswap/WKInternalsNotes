# ``WKInternalsNotes/WKContentView/_didChangeWebViewEditability()``

WebView の編集可否変更に応じて UI を更新する。

## Objective-C Declaration
```objective-c
- (void)_didChangeWebViewEditability;
```

## Discussion
アクセサリの次/前ボタン表示や二本指タップの有効/無効を更新し、編集可の場合は `UITextInputMultiDocument` をプロトコル追加する。

## References
- [`WKContentViewInteraction.h#L856`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L856)
- [`WKContentViewInteraction.mm#L6415`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6415)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
