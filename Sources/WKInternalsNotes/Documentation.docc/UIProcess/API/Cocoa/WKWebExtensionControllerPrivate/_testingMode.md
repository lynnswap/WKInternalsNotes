# ``WKInternalsNotes/WKWebExtensionController/_testingMode``

テストモードの有効/無効を示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=_inTestingMode, setter=_setTestingMode:) BOOL _testingMode;
```

## Default Value
`NDEBUG` 定義時は `NO`、それ以外は `YES`（内部 `WebExtensionController` の既定値）。

## Discussion
getter は `_webExtensionController->inTestingMode()` を返し、setter は `setTestingMode` に委譲する。

## References
- [`WKWebExtensionControllerPrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerPrivate.h#L36)
- [`WKWebExtensionController.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionController.mm)
- [`WebExtensionController.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/WebExtensionController.h#L119)
- [`WebExtensionController.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/WebExtensionController.h#L119)
- [`WebExtensionController.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/WebExtensionController.h#L119)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
