# ``WKInternalsNotes/_WKFocusedElementInfo/label``

関連するラベル文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *label;
```

## Default Value
`FocusedElementInformation::label` の値。

## Discussion
初期化時に `information.label` を `NSString` 化して保持し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L76)
- [`WKContentViewInteraction.mm#L1014`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1014)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
