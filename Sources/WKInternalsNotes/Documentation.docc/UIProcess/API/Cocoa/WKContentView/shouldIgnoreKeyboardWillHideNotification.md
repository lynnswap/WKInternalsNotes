# ``WKInternalsNotes/WKContentView/shouldIgnoreKeyboardWillHideNotification``

キーボードの willHide 通知を無視すべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL shouldIgnoreKeyboardWillHideNotification;
```

## Default Value
回転中やフォーカス遷移中は `YES`。

## Discussion
回転中 (`UIPeripheralHost.sharedInstance.rotationState`) か、フォーカス変更中にキーボードを表示している場合は `YES`。それ以外は `NO`。

## References
- [`WKContentViewInteraction.h#L723`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L723)
- [`WKContentViewInteraction.mm#L8730`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8730)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
