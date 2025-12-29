# ``WKInternalsNotes/_WKTargetedElementInfo/pseudoElement``

疑似要素かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isPseudoElement) BOOL pseudoElement;
```

## Default Value
`API::TargetedElementInfo::isPseudoElement()` の値。

## Discussion
内部の `_info` から `isPseudoElement()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L47)
- [`_WKTargetedElementInfo.mm#L177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L177)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
