# ``WKInternalsNotes/WKSharingServicePickerDelegate/menuProxy()``

`WebContextMenuProxyMac` への弱参照を返す。

## Objective-C Declaration
```objective-c
- (WebKit::WebContextMenuProxyMac*)menuProxy;
```

## Discussion
`_menuProxy.get()` を返すだけの実装。

## References
- [`WKSharingServicePickerDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKSharingServicePickerDelegate.h#L48)
- [`WKSharingServicePickerDelegate.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKSharingServicePickerDelegate.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
