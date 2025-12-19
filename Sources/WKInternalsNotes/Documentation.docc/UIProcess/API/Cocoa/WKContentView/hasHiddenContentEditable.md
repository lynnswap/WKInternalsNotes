# ``WKInternalsNotes/WKContentView/hasHiddenContentEditable()``

隠れた contenteditable 状態があるかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)hasHiddenContentEditable;
```

## Discussion
`_suppressSelectionAssistantReasons` に透明/極小要素の理由が含まれているかで判定する。

## References
- [`WKContentViewInteraction.h#L862`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L862)
- [`WKContentViewInteraction.mm#L9560`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9560)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
