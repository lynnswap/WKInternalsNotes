# ``WKInternalsNotes/WKContentView/_hardwareKeyboardAvailabilityChanged()``

ハードウェアキーボードの利用可否変更を処理する。

## Objective-C Declaration
```objective-c
- (void)_hardwareKeyboardAvailabilityChanged;
```

## Discussion
`_seenHardwareKeyDownInNonEditableElement` を `NO` に戻し、`reloadInputViews` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L816`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L816)
- [`WKContentViewInteraction.mm#L8744`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8744)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
