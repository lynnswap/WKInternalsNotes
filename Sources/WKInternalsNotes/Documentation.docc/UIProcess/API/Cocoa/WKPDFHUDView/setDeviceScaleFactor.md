# ``WKInternalsNotes/WKPDFHUDView/setDeviceScaleFactor(_:)``

デバイススケールを更新する。

## Objective-C Declaration
```objective-c
- (void)setDeviceScaleFactor:(CGFloat)deviceScaleFactor;
```

## Discussion
値が変わらない場合は何もしない。変更がある場合は `_deviceScaleFactor` を更新してレイヤーを再描画する。

## References
- [`WKPDFHUDView.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.mm#L146)
- [`WKPDFHUDView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
