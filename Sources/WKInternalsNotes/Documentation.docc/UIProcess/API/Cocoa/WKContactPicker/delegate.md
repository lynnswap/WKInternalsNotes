# ``WKInternalsNotes/WKContactPicker/delegate``

連絡先ピッカーの表示/非表示通知を受け取るデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id<WKContactPickerDelegate> delegate;
```

## Default Value
`nil`。

## Discussion
内部では `WeakObjCPtr` として保持し、提示完了時に `contactPickerDidPresent:`、終了時に `contactPickerDidDismiss:` を通知する。

## References
- [`WKContactPicker.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L53)
- [`WKContactPicker.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L136)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
