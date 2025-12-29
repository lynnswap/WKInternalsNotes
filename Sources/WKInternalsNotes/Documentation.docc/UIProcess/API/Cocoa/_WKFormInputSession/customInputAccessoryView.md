# ``WKInternalsNotes/_WKFormInputSession/customInputAccessoryView``

カスタムの input accessory view を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIView *customInputAccessoryView WK_API_AVAILABLE(ios(12.2));
```

## Default Value
`nil`。

## Discussion
setter で変更があれば保持して `reloadInputViews` を呼び、getter は保持している `UIView` を返す。

## References
- [`WKContentViewInteraction.mm#L859`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L859)
- [`WKContentViewInteraction.mm#L864`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L864)
- [`_WKFormInputSession.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
