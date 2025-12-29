# ``WKInternalsNotes/_WKFormInputSession/customInputView``

カスタムの input view を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIView *customInputView WK_API_AVAILABLE(ios(10.0));
```

## Default Value
`nil`。

## Discussion
setter で変更があれば保持して `reloadInputViews` を呼び、getter は保持している `UIView` を返す。

## References
- [`WKContentViewInteraction.mm#L845`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L845)
- [`WKContentViewInteraction.mm#L850`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L850)
- [`_WKFormInputSession.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
