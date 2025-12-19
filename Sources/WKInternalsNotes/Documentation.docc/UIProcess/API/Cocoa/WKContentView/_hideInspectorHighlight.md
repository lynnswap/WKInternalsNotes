# ``WKInternalsNotes/WKContentView/_hideInspectorHighlight()``

インスペクタのハイライト表示を終了する。

## Objective-C Declaration
```objective-c
- (void)_hideInspectorHighlight;
```

## Discussion
`_inspectorHighlightView` があれば `removeFromSuperview` して `nil` にする。

## References
- [`WKContentView.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L126)
- [`WKContentView.mm#L622`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L622)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
