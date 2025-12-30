# ``WKInternalsNotes/WKSharingServicePickerDelegate/removeBackground()``

管理している画像の背景除去を要求する。

## Objective-C Declaration
```objective-c
- (void)removeBackground;
```

## Discussion
`_menuProxy` が存在する場合に `removeBackgroundFromControlledImage()` を呼ぶ。

## References
- [`WKSharingServicePickerDelegate.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKSharingServicePickerDelegate.h#L55)
- [`WKSharingServicePickerDelegate.mm#L189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKSharingServicePickerDelegate.mm#L189)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
