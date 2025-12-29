# ``WKInternalsNotes/_WKFocusedElementInfo/userObject``

フォーカス要素に関連付けられたユーザーオブジェクトを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSObject <NSSecureCoding> *userObject WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
`initWithFocusedElementInformation` の `userObject` 引数の値。

## Discussion
初期化時に `userObject` を保持し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L89)
- [`WKContentViewInteraction.mm#L1009`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1009)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
