# ``WKInternalsNotes/WKFormPeripheralBase/endEditing()``

編集終了を通知する。

## Objective-C Declaration
```objective-c
- (void)endEditing;
```

## Discussion
編集中でない場合は何もしない。編集中なら `_editing` を `NO` にして `controlEndEditing` を呼ぶ。

## References
- [`WKFormPeripheralBase.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L66)
- [`WKFormPeripheralBase.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
