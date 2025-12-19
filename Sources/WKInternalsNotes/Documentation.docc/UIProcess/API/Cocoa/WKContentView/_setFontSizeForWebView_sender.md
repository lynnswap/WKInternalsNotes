# ``WKInternalsNotes/WKContentView/_setFontSizeForWebView(_:sender:)``

フォントサイズを変更する。

## Objective-C Declaration
```objective-c
- (void)_setFontSizeForWebView:(CGFloat)fontSize sender:(id)sender;
```

## Discussion
サイズのみ設定した `FontChanges` を作成し、`changeFont` を呼び出す。

## References
- [`WKContentViewInteraction.h#L786`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L786)
- [`WKContentViewInteraction.mm#L4548`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4548)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
