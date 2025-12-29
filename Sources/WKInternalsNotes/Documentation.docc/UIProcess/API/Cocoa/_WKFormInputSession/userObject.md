# ``WKInternalsNotes/_WKFormInputSession/userObject``

フォーカス要素に紐づくユーザーオブジェクトを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSObject <NSSecureCoding> *userObject;
```

## Default Value
`nil`。

## Discussion
`focusedElementInfo` の `userObject` をそのまま返す。

## References
- [`WKContentViewInteraction.mm#L792`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L792)
- [`_WKFormInputSession.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
