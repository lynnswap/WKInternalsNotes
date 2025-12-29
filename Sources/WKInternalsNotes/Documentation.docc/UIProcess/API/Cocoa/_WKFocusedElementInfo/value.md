# ``WKInternalsNotes/_WKFocusedElementInfo/value``

フォーカス時点の値を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *value;
```

## Default Value
`FocusedElementInformation::value` の値。

## Discussion
初期化時に `information.value` を `NSString` 化して保持し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L70)
- [`WKContentViewInteraction.mm#L999`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L999)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
