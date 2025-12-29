# ``WKInternalsNotes/WKFormPeripheralBase/updateEditing()``

編集内容の更新を通知する。

## Objective-C Declaration
```objective-c
- (void)updateEditing;
```

## Discussion
編集中でない場合は何もしない。編集中なら `controlUpdateEditing` を呼ぶ。

## References
- [`WKFormPeripheralBase.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L58)
- [`WKFormPeripheralBase.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
