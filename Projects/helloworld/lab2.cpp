#include "lusb0_usb.h" // LibUsb 
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <conio.h>
#include <Windows.h>
#include <stdlib.h>

using namespace std;

void print_device_desc(struct usb_device_descriptor* device)
{
	cout << left << setw(24) << dec << "  bLength: " << int(device->bLength) << endl;
	cout << left << hex << setw(24) << "  bDescriptorType: " << int(device->bDescriptorType) << "h" << endl;
	cout << left << hex << setw(24) << "  bcdUSB: " << int(device->bcdUSB) << "h" << endl;
	cout << left << hex << setw(24) << "  bDeviceClass: " << int(device->bDeviceClass) << "h" << endl;
	cout << left << hex << setw(24) << "  bDeviceSubClass: " << int(device->bDeviceSubClass) << "h" << endl;
	cout << left << hex << setw(24) << "  bDeviceProtocol: " << int(device->bDeviceProtocol) << "h" << endl;
	cout << left << hex << setw(24) << "  bMaxPacketSize0: " << int(device->bMaxPacketSize0) << "h" << endl;
	cout << left << hex << setw(24) << "  idVendor: " << int(device->idVendor) << "h" << endl;
	cout << left << hex << setw(24) << "  idProduct: " << int(device->idProduct) << "h" << endl;
	cout << left << hex << setw(24) << "  bcdDevice: " << int(device->bcdDevice) << "h" << endl;

	return;
}

void print_config_desc(struct usb_config_descriptor *config)
{
	cout << left << setw(27) << "    wTotalLength: " << config->wTotalLength << endl;
	cout << left << setw(27) << "    bNumInterfaces: " << int(config->bNumInterfaces) << endl;
	cout << left << setw(27) << "    bConfigurationValue: " << int(config->bConfigurationValue) << endl;
	cout << left << setw(27) << "    iConfiguration: " << int(config->iConfiguration) << endl;
	cout << left << setw(27) << hex << "    bmAttributes: " << int(config->bmAttributes) << "h" << endl;
	cout << left << setw(27) << "    MaxPower: " << int(config->MaxPower) << endl;

	return;
}

void print_interface_desc(struct usb_interface_descriptor* interface)
{
	cout << left << setw(30) << "       bInterfaceNumber: " << int(interface->bInterfaceNumber) << endl;
	cout << left << setw(30) << "       bAlternateSetting: " << int(interface->bAlternateSetting) << endl;
	cout << left << setw(30) << "       bNumEndpoints: " << int(interface->bNumEndpoints) << endl;
	cout << left << setw(30) << "       bInterfaceClass: " << int(interface->bInterfaceClass) << endl;
	cout << left << setw(30) << "       bInterfaceSubClass: " << int(interface->bInterfaceSubClass) << endl;
	cout << left << setw(30) << "       bInterfaceProtocol: " << int(interface->bInterfaceProtocol) << endl;
	cout << left << setw(30) << "       iInterface: " << int(interface->iInterface) << endl;

	return;
}

void print_endpoint_desc(struct usb_endpoint_descriptor* endpoint)
{
	cout << left << setw(33) << hex << "          bEndpointAddress: " << int(endpoint->bEndpointAddress) << "h" << endl;
	cout << left << setw(33) << hex << "          bmAttributes: " << int(endpoint->bmAttributes) << "h" << endl;
	cout << left << setw(33) << "          wMaxPacketSize: " << int(endpoint->wMaxPacketSize) << endl;
	cout << left << setw(33) << "          bInterval: " << int(endpoint->bInterval) << endl;
	cout << left << setw(33) << "          bRefresh: " << int(endpoint->bRefresh) << endl;
	cout << left << setw(33) << "          bSynchAddress: " << int(endpoint->bSynchAddress) << endl << endl;

	return;
}

void print_device(struct usb_device *dev)
{
	usb_dev_handle *udev;
	char string[256];
	udev = usb_open(dev);
	if (udev == 0)
	{
		cout << "���������� ������� USB-���������� " << usb_strerror() << endl;
		return;
	}

	cout << hex << uppercase << "Device VID: " << dev->descriptor.idVendor << endl; // VID

	cout << hex << uppercase << "Device PID: " << dev->descriptor.idProduct << endl; // PID

	usb_get_string_simple(udev, dev->descriptor.iManufacturer, string, 256);
	cout << "Manufacturer: " << string << endl;

	usb_get_string_simple(udev, dev->descriptor.iProduct, string, 256);
	cout << "Product: " << string << endl;

	usb_get_string_simple(udev, dev->descriptor.iSerialNumber, string, sizeof(string));
	cout << "Serial Number: " << string << endl;

	print_device_desc(&dev->descriptor);

	for (int i = 0; i < int(dev->descriptor.bNumConfigurations); i++)
	{
		print_config_desc(&dev->config[i]);
	}

	for (int i = 0; i < int(dev->config->bNumInterfaces); i++)
	{
		print_interface_desc(&dev->config->interface->altsetting[i]);
	}

	for (int i = 0; i < int(dev->config->interface->altsetting->bNumEndpoints); i++)
	{
		print_endpoint_desc(&dev->config->interface->altsetting->endpoint[i]);
	}

	return;
}

int main()
{

	while (true)
	{
		int chet = 0;
		int chet2 = 0;
		setlocale(LC_ALL, "rus");
		usb_init(); 
		usb_find_busses();
		usb_find_devices();
		usb_bus *bus;
		for (bus = usb_busses; bus; bus = bus->next)
		{

			struct usb_device *dev;
			for (dev = bus->devices; dev; dev = dev->next)
			{
				chet++;
				print_device(dev);
				cout << "/-------------------------------------------/\n" << endl;
			}
		}
		chet2 = chet;
		while (chet == chet2)
		{
			chet2 = 0;
			usb_init();
			usb_find_busses();
			usb_find_devices();
			usb_bus *bus;
			for (bus = usb_busses; bus; bus = bus->next)
			{
				struct usb_device *dev;
				for (dev = bus->devices; dev; dev = dev->next)
				{
					chet2++;
				}
			}
		}
		system("cls");
	}
	system("pause");
	return 0;
}