# ``WKInternalsNotes/_WKFocusedElementInfo/placeholder``

プレースホルダ文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *placeholder;
```

## Default Value
`FocusedElementInformation::placeholder` の値。

## Discussion
初期化時に `information.placeholder` を `NSString` 化して保持し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L73)
- [`WKContentViewInteraction.mm#L1019`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1019)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
