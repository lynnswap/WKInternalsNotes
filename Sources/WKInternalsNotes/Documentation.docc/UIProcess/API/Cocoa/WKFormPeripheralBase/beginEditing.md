# ``WKInternalsNotes/WKFormPeripheralBase/beginEditing()``

編集開始を通知する。

## Objective-C Declaration
```objective-c
- (void)beginEditing;
```

## Discussion
既に編集中なら何もしない。未編集なら `_editing` を `YES` にして `controlBeginEditing` を呼ぶ。

## References
- [`WKFormPeripheralBase.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L49)
- [`WKFormPeripheralBase.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
