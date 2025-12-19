# ``WKInternalsNotes/WKInspectorViewController/didAttachOrDetach()``

Inspector のアタッチ状態変化を反映する。

## Objective-C Declaration
```objective-c
- (void)didAttachOrDetach;
```

## Discussion
`CONTENT_INSET_BACKGROUND_FILL` 有効時に、水平アタッチ先の WebView の top pocket 情報を反映し、スクロールポケットの表示を更新する。

## References
- [`WKInspectorViewController.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L51)
- [`WKInspectorViewController.mm#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.mm#L229)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
