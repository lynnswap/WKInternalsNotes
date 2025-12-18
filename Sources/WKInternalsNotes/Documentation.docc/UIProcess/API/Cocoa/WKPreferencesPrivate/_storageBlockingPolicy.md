# ``WKInternalsNotes/WKPreferences/_storageBlockingPolicy``

Storage Blocking Policy を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setStorageBlockingPolicy:) _WKStorageBlockingPolicy _storageBlockingPolicy;
```

## Default Value
iOS: `WebCore::StorageBlockingPolicy::BlockThirdParty` / macOS: `WebCore::StorageBlockingPolicy::BlockThirdParty`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_storageBlockingPolicy` を設定すると: Storage Blocking Policy を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Document.cpp#L719`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L719) の `InspectorInstrumentation::addEventListenersToNode` が `storageBlockingPolicy()` を参照する。

## Details
- WebPreferences key: `StorageBlockingPolicy`

## References
- [`WKPreferencesPrivate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L73)
- [`WKPreferences.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L286)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L7685`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7685) (key: `StorageBlockingPolicy`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
