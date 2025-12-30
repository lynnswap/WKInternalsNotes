# ``WKInternalsNotes/WKSharingServicePickerDelegate/sharedSharingServicePickerDelegate()``

シングルトンの delegate インスタンスを返す。

## Objective-C Declaration
```objective-c
+ (WKSharingServicePickerDelegate *)sharedSharingServicePickerDelegate;
```

## Discussion
`NeverDestroyed` の静的インスタンスを生成して返す。

## References
- [`WKSharingServicePickerDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKSharingServicePickerDelegate.h#L47)
- [`WKSharingServicePickerDelegate.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKSharingServicePickerDelegate.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
